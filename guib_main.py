#!/usr/bin/python3
import numpy as np

def NormalProductOnDoors(circuit1 :np.ndarray, circuit2: np.ndarray) -> np.ndarray:
    return circuit2 @ circuit1

def tensorProductOnDoors(circuit1 :np.ndarray, circuit2: np.ndarray) -> np.ndarray:
        return np.kron(circuit2, circuit1)

#Fonction qui ajoute une version contrôlé d'une porte quantique (argument1:)

#Fonction qui réorganise les qubits d'une porte quantique (argument1: porte, argument2: ordre des qubits)

#Définition d'un classe pour les opérations courantes
#---------------------------------------------------------------------------------------------
class QuantumOperations:
    init_state = None

    def init_a_state(self, init_state: np.ndarray) -> np.ndarray:
        return self.state

    def tensorProductOnSelfAsCircuit1(self, circuit2: np.ndarray) -> np.ndarray:
        return np.kron(circuit2, self)

    def tensorProductOnSelfAsCircuit2(self, circuit1: np.ndarray) -> np.ndarray:
        return np.kron(self, circuit1)

    def NormalProductOnSelfAsCircuit1(self, circuit2: np.ndarray) -> np.ndarray:
        return circuit2 @ self

    def NormalProductOnSelfAsCircuit2(self, circuit1: np.ndarray) -> np.ndarray:
        return self @ circuit1
# Fin Class QuantumOperations ----------------------------------------------------------------
#----------------------------------------------------------------------------------------------

if __name__== "__main__":
    # Définitions des portes quantiques à deux qubits
    i_gate = np.array([[1,0],[0,1]])
    x_gate = np.array([[0,1],[1,0]])
    h_gate = np.sqrt(0.5) * np.array([[1,1],[1,-1]])
    cx_gate = np.array([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])
    #Produits tensoriels de portes quantiques
    ih_gate = np.kron(i_gate, h_gate)
    #Paire de Bell, état produit des portes quantiques cx_gate multiplié par ih_gate
    b_circuit = cx_gate @ ih_gate

#-------------------------------------------------------------------------------------------------
    # Opérations préparatoires à 1 et 2 qubits
    init_state_0 = np.array([1,0,0,0]).T
    init_state_i = np.array([1j,0,0,0]).T
    b_state_from_0 = b_circuit @ init_state_0
    b_state_from_j = b_circuit @ init_state_i
    probabilities_b_state_from_0  = b_state_from_0 * np.conjugate(b_state_from_0)
    probabilities_b_state_from_j  = np.real(b_state_from_j * np.conjugate(b_state_from_j))
    probabilities_b_state_from_0_imag  = np.imag(b_state_from_0 * np.conjugate(b_state_from_0))
    print(b_state_from_0)
    print(probabilities_b_state_from_0)
    print(probabilities_b_state_from_0_imag)
    print(b_state_from_j)
    print(probabilities_b_state_from_j)
    print(type(init_state_0))
#---------------------------------------------------------------------------------------------------
# Premier circuit, la porte du trésor
    treasure_door = QuantumOperations()
    
