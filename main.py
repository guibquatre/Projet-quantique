#!/usr/bin/python3
import numpy as np

# Les exceptions ne sont pas encore gérées, à utiliser avec précaution
def normalProductOnDoors(circuit1 :np.ndarray, circuit2: np.ndarray) -> np.ndarray:
    return circuit2 @ circuit1

def tensorProductOnDoors(circuit1 :np.ndarray, circuit2: np.ndarray) -> np.ndarray:
        return np.kron(circuit2, circuit1)

#TO DO
#Fonction qui ajoute une version contrôlé d'une porte quantique (argument1: circuit||Porte)

#TO DO
#Fonction qui réorganise les qubits d'une porte quantique (argument1: porte, argument2: ordre des qubits)


#Définition d'un classe pour les opérations courantes
#---------------------------------------------------------------------------------------------
class QuantumOperations:
    init_state = None

    def __init__(self, _init_state: np.ndarray) -> np.ndarray:
        self.init_state = _init_state.T

    def tensorProductOnSelfAsCircuit1(self, circuit2: np.ndarray) -> np.ndarray:
        return np.kron(circuit2, self.init_state)

    def tensorProductOnSelfAsCircuit2(self, circuit1: np.ndarray) -> np.ndarray:
        return np.kron(self.init_state, circuit1)

    def normalProductOnSelfAsCircuit1(self, circuit2: np.ndarray) -> np.ndarray:
        return circuit2 @ self.init_state

    def normalProductOnSelfAsCircuit2(self, circuit1: np.ndarray) -> np.ndarray:
        return self.init_state @ circuit1
# Fin Class QuantumOperations ----------------------------------------------------------------
#----------------------------------------------------------------------------------------------

if __name__== "__main__":
    # Définitions des portes quantiques à deux qubits
    i_gate = np.array([[1,0],[0,1]])
    x_gate = np.array([[0,1],[1,0]])
    h_gate = np.sqrt(0.5) * np.array([[1,1],[1,-1]])
    cx_gate = np.array([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])
# Opérations vues en classe
#-------------------------------------------------------------------------------------------------
    # Opérations préparatoires à 1 et 2 qubits
    # init_state_0 = np.array([1,0,0,0]).T
    # init_state_i = np.array([1j,0,0,0]).T
    # b_state_from_0 = b_circuit @ init_state_0
    # b_state_from_j = b_circuit @ init_state_i
    # probabilities_b_state_from_0  = b_state_from_0 * np.conjugate(b_state_from_0)
    # probabilities_b_state_from_j  = np.real(b_state_from_j * np.conjugate(b_state_from_j))
    # probabilities_b_state_from_0_imag  = np.imag(b_state_from_0 * np.conjugate(b_state_from_0))
    # print(b_state_from_0)
    # print(probabilities_b_state_from_0)
    # print(probabilities_b_state_from_0_imag)
    # print(b_state_from_j)
    # print(probabilities_b_state_from_j)
    # print(type(init_state_0))
#---------------------------------------------------------------------------------------------------
# Premier circuit, la porte du trésor
    #Création objet et état initial
    treasure_door = QuantumOperations(np.array([1,0,0,0,0,0,0,0]))
    assert(np.array_equal(treasure_door.init_state, np.array([1,0,0,0,0,0,0,0])))
    #Produit tensoriel entre une porte h et une identité à un qubit 
    ih_gate = tensorProductOnDoors(h_gate, i_gate)
    #Construire circuit de Bell, produit des portes quantiques cx_gate multiplié par ih_gate
    b_circuit = normalProductOnDoors(ih_gate, cx_gate)
    premierPalierTreasureDoorCircuit = tensorProductOnDoors(b_circuit, h_gate)
    premierPalierTreasureDoorState = treasure_door.normalProductOnSelfAsCircuit1(premierPalierTreasureDoorCircuit)
    print(premierPalierTreasureDoorState)
    # Construire porte c_not à l'envers
    xc_gate = tensorProductOnDoors(i_gate, x_gate)
    np.testing.assert_equal(np.any(np.not_equal(xc_gate, cx_gate)), True)
    