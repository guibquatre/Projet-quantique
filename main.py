#!/usr/bin/python3
import numpy as np
from functools import wraps
import traceback
import sys

def normalProductOnDoors(circuit1 :np.ndarray, circuit2: np.ndarray) -> np.ndarray:
    try:
        return circuit1 @ circuit2
    except Exception as e:
        print("Problème avec normalProductOnDoors")
        # traceback.print_exc()
        sys.exit(1)

def tensorProductOnDoors(circuit1 :np.ndarray, circuit2: np.ndarray) -> np.ndarray:
    try:
        return np.kron(circuit1, circuit2)
    except Exception as e:
        print("Problème avec tensorProductOnDoors")
        # traceback.print_exc()
        sys.exit(1)    

#TO DO
#Fonction qui ajoute une version contrôlé d'une porte quantique (argument1: circuit||Porte)

#TO DO
#Fonction qui réorganise les qubits d'une porte quantique (argument1: porte, argument2: ordre des qubits)


#Définition d'un classe pour les opérations courantes
#---------------------------------------------------------------------------------------------
class QuantumOperations:
    init_state = None

    # S'assurer que l'état initital n'est pas autre chose qu'une np.ndarray()
    def np_ndarray_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not isinstance(args[1], np.ndarray):
                print("utilisez numpy pour créer un état initial")
                sys.exit(1)
            return f(*args, **kwargs)
        return decorated

    @np_ndarray_required
    def __init__(self, _init_state: np.ndarray) -> np.ndarray:
        try:
            self.init_state = _init_state.T
        except Exception as e:
            print("Problème avec constructeur de QuantumOperations")
            # traceback.print_exc()
            sys.exit(1)

    def tensorProductOnSelfAsCircuit1(self, circuit2: np.ndarray) -> np.ndarray:
        try:
            return np.kron(circuit2, self.init_state)
        except Exception as e:
            print("Problème avec tensorProductOnSelfAsCircuit1")
            # traceback.print_exc()
            sys.exit(1)

    def tensorProductOnSelfAsCircuit2(self, circuit1: np.ndarray) -> np.ndarray:
        try:
            return np.kron(self.init_state, circuit1)
        except Exception as e:
            print("Problème avec tensorProductOnSelfAsCircuit2")
            # traceback.print_exc()
            sys.exit(1)

    def normalProductOnSelfAsCircuit1(self, circuit2: np.ndarray) -> np.ndarray:
        try:
            return circuit2 @ self.init_state
        except Exception as e:
            print("Problème avec normalProductOnSelfAsCircuit1")
            # traceback.print_exc()
            sys.exit(1)

    def normalProductOnSelfAsCircuit2(self, circuit1: np.ndarray) -> np.ndarray:
        try:
            return self.init_state @ circuit1
        except Exception as e:
            print("Problème avec normalProductOnSelfAsCircuit2")
            # traceback.print_exc()
            sys.exit(1)
# Fin Class QuantumOperations ----------------------------------------------------------------
#----------------------------------------------------------------------------------------------
# Application principale
if __name__== "__main__":
    # Définitions des portes quantiques à un et deux qubits
    i_gate = np.array([[1,0],[0,1]])
    x_gate = np.array([[0,1],[1,0]])
    h_gate = np.sqrt(0.5) * np.array([[1,1],[1,-1]])
    #Produit tensoriel entre une porte h et une identité à un qubit 
    ih_gate = tensorProductOnDoors(i_gate, h_gate)
    xi_gate = tensorProductOnDoors(x_gate, i_gate)
    xii_gate = tensorProductOnDoors(xi_gate, i_gate)
    cx_gate = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    xc_gate = np.array([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])
    swap_gate = normalProductOnDoors(normalProductOnDoors(xc_gate, cx_gate), xc_gate)
    xx_gate = tensorProductOnDoors(x_gate, x_gate)
    # Trois qubits
    # |ψ⟩ = α |000⟩ + β |001⟩ + γ |010⟩ + δ |011⟩ + ε |100⟩ + ζ |101⟩ + η |110⟩ + θ |111⟩ .
    cix_gate = np.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0]])
# TO DO
# Porte swap 
    # cx_gate2 = np.array([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])
    # np.testing.assert_equal(np.any(np.not_equal(cx_gate, xc_gate)), True)
    # np.testing.assert_equal(cx_gate, cx_gate2)
#-------------------------------------------------------------------------------------------------
# Opérations préparatoires vues en cours à 1 et 2 qubits
    # init_state_0 = np.array([1,0,0,0]).T
    # init_state_i = np.array([1j,0,0,0]).T
    # b_state_from_0 = b_circuit @ init_state_0
    # b_state_from_j = b_circuit @ init_state_i
    # probabilities_b_state_from_0  = b_state_from_0 * np.conjugate(b_state_from_0)
    # probabilities_b_state_from_j  = np.real(b_state_from_j * np.conjugate(b_state_from_j))
    # probabilities_b_state_from_0_imag  = np.imag(b_state_from_0 * np.conjugate(b_state_from_0))
#---------------------------------------------------------------------------------------------------
# Premier circuit, la porte du trésor
# Premier pallier
    #Création objet et état initial
    treasure_door = QuantumOperations(np.array([1,0,0,0,0,0,0,0]))
    assert(np.array_equal(treasure_door.init_state, np.array([1,0,0,0,0,0,0,0])))
    #Construire circuit de Bell, produit des portes quantiques cx_gate multiplié par ih_gate
    b_circuit = normalProductOnDoors(xc_gate, ih_gate)
    circuit_1er_palier = tensorProductOnDoors(h_gate, b_circuit)
    # Premier palier produit
    treasure_door.init_state = treasure_door.normalProductOnSelfAsCircuit1(circuit_1er_palier)
    # print(treasure_door.init_state)
    # Tester le décorateur, utilisez numpy pour créer un état initial devrait s'écrire au terminal
    # erreur = QuantumOperations(8)
#----------------------------------------------------------------------------------------------------------
# Deuxieme palier
    xi_cx_circuit = normalProductOnDoors(xi_gate, cx_gate)
    xi_cx_i_gate = tensorProductOnDoors(xi_cx_circuit, i_gate)
    cix__xi_cx_i_circuit = normalProductOnDoors(cix_gate, xi_cx_i_gate)
    circuit_2e_palier = normalProductOnDoors(xii_gate, cix__xi_cx_i_circuit)
    treasure_door.init_state = treasure_door.normalProductOnSelfAsCircuit1(circuit_2e_palier)
    # print(treasure_door.init_state)
# Troisieme palier
    circuit_3e_Palier = tensorProductOnDoors(i_gate, normalProductOnDoors(xx_gate, swap_gate))
    treasure_door.init_state = treasure_door.normalProductOnSelfAsCircuit1(circuit_3e_Palier)
    # print(treasure_door.init_state)
# Quatrième et dernier palier
    print(normalProductOnDoors(treasure_door.init_state, circuit_2e_palier))
# Fin porte au trésor-------------------------------------------------------------------------------------