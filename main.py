#!/usr/bin/python3
import numpy as np
from functools import wraps
import traceback
import sys
from matplotlib import pyplot as plt
import math  
NEGATE_THE_NUMBER = -1
RY_GATE_ANGLE_MONTY_HALL = 2*math.acos(1/math.sqrt(3))
UN_SUR_RACINE_DE_DEUX = 1/math.sqrt(2)

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

def ry_gate_function(θ: float) -> np.ndarray:
    return np.array([[math.cos(θ/2), (math.sin(θ/2)*NEGATE_THE_NUMBER)],\
                    [math.sin(θ/2), math.cos(θ/2)]])

#TODO
#Fonction qui ajoute une version contrôlé d'une porte quantique (argument1: circuit||Porte)

#TODO
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
            traceback.print_exc()
            sys.exit(1)

    def normalProductOnSelfAsCircuit2(self, circuit1: np.ndarray) -> np.ndarray:
        try:
            return self.init_state @ circuit1
        except Exception as e:
            print("Problème avec normalProductOnSelfAsCircuit2")
            # traceback.print_exc()
            sys.exit(1)

    def getProbabilitiesOfInitState(self):
        try:
            print("Probabilities: ",(self.init_state * np.conjugate(self.init_state)))
            return self.init_state * np.conjugate(self.init_state)
        except Exception as e:
            print("Problème avec getProbabilitiesOfInitState")
            # traceback.print_exc()
            sys.exit(1)
    
    # TODO Verifier le nombre de qubits avec un décorateur
    def sample_state_3qubits(self, shots: int) -> dict:
        probabilities  = self.getProbabilitiesOfInitState()
        components = ["α", "β", "γ", "δ", "ε", "ζ", "η", "θ"]
        results = np.random.choice(components, shots, p=probabilities)
        index = 0
        dictOfResults = dict()
        dictOfResults["α"] = 0
        dictOfResults["β"] = 0
        dictOfResults["γ"] = 0
        dictOfResults["δ"] = 0
        dictOfResults["ε"] = 0
        dictOfResults["ζ"] = 0
        dictOfResults["η"] = 0
        dictOfResults["θ"] = 0
        while index < results.size:
            match results[index]:
                case "α":
                    dictOfResults["α"]+=1
                case "β":
                    dictOfResults["β"]+=1
                case "γ":
                    dictOfResults["γ"]+=1
                case "δ":
                    dictOfResults["δ"]+=1
                case "ε":
                    dictOfResults["ε"]+=1        
                case "ζ":
                    dictOfResults["ζ"]+=1
                case "η":
                    dictOfResults["η"]+=1
                case "θ":
                    dictOfResults["θ"]+=1
                case _:
                    print("une erreur s'est produite au moment de compiler les résultats")
            index+=1
        return dictOfResults

    # TODO Verifier le nombre de qubits avec un décorateur
    def sample_state_4qubits(self, shots: int) -> dict:
        probabilities  = self.getProbabilitiesOfInitState()
        components = ["α", "β", "γ", "δ", "ε", "ζ", "η", "θ", "α1", "β1", "γ1", "δ1", "ε1", "ζ1", "η1", "θ1"]
        results = np.random.choice(components, shots, p=probabilities)
        index = 0
        dictOfResults = dict()
        dictOfResults["α"], dictOfResults["β"], dictOfResults["γ"], dictOfResults["δ"] = 0
        dictOfResults["ε"], dictOfResults["ζ"], dictOfResults["η"], dictOfResults["θ"] = 0
        dictOfResults["α1"], dictOfResults["β1"], dictOfResults["γ1"], dictOfResults["δ1"] = 0
        dictOfResults["ε1"], dictOfResults["ζ1"], dictOfResults["η1"], dictOfResults["θ1"] = 0
        while index < results.size:
            match results[index]:
                case "α":
                    dictOfResults["α"]+=1
                case "β":
                    dictOfResults["β"]+=1
                case "γ":
                    dictOfResults["γ"]+=1
                case "δ":
                    dictOfResults["δ"]+=1
                case "ε":
                    dictOfResults["ε"]+=1        
                case "ζ":
                    dictOfResults["ζ"]+=1
                case "η":
                    dictOfResults["η"]+=1
                case "θ":
                    dictOfResults["θ"]+=1
                case "α1":
                    dictOfResults["α1"]+=1
                case "β1":
                    dictOfResults["β1"]+=1
                case "γ1":
                    dictOfResults["γ1"]+=1
                case "δ1":
                    dictOfResults["δ1"]+=1
                case "ε1":
                    dictOfResults["ε1"]+=1        
                case "ζ1":
                    dictOfResults["ζ1"]+=1
                case "η1":
                    dictOfResults["η1"]+=1
                case "θ1":
                    dictOfResults["θ1"]+=1
                case _:
                    print("une erreur s'est produite au moment de compiler les résultats")
            index+=1
        return dictOfResults
    
    def show(self, _dictOfResults: dict):
        print(_dictOfResults)
        plt.title("stateVectors") 
        plt.bar(*zip(*_dictOfResults.items()))
        plt.show()


# Fin Class QuantumOperations ----------------------------------------------------------------
#----------------------------------------------------------------------------------------------
# Application principale
if __name__== "__main__":
    # Définitions des portes quantiques
    i_gate = np.array([[1,0],[0,1]])
    x_gate = np.array([[0,1],[1,0]])
    h_gate = np.sqrt(0.5) * np.array([[1,1],[1,-1]])
    ih_gate = tensorProductOnDoors(i_gate, h_gate)
    xi_gate = tensorProductOnDoors(x_gate, i_gate)
    xii_gate = tensorProductOnDoors(xi_gate, i_gate)
    cx_gate = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    xc_gate = np.array([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])
    hc_gate = np.array([[1,0,0,0],[0, UN_SUR_RACINE_DE_DEUX, 0, UN_SUR_RACINE_DE_DEUX],\
                        [0,0,1,0],[0, UN_SUR_RACINE_DE_DEUX, 0, UN_SUR_RACINE_DE_DEUX*NEGATE_THE_NUMBER]])
    xiic_gate = np.array([[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
                        [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],\
                        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],\
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],\
                        [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],\
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],\
                        [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],\
                        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],\
                        [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
                        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],\
                        [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],\
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],\
                        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],\
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],\
                        [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]])
    swap_gate = normalProductOnDoors(normalProductOnDoors(xc_gate, cx_gate), xc_gate)
    xx_gate = tensorProductOnDoors(x_gate, x_gate)
    # Trois qubits
    # |ψ⟩ = α |000⟩ + β |001⟩ + γ |010⟩ + δ |011⟩ + ε |100⟩ + ζ |101⟩ + η |110⟩ + θ |111⟩ .
    cix_gate = np.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0]])
    # cx_gate_again_for_tests = np.array([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])
    # np.testing.assert_equal(np.any(np.not_equal(cx_gate, xc_gate)), True)
    # np.testing.assert_equal(cx_gate, cx_gate_again_for_tests)
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
    #u_circuit = np.matmul(cx_gate, ih_gate)
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
    treasure_door.init_state = normalProductOnDoors(treasure_door.init_state, circuit_2e_palier)
    # print("treasure_door: ", treasure_door.init_state)
# Fin porte au trésor----------------------------------------------------------------------------------------
# Start counts for treasure door-----------------------------------------------------------------------------
    # treasure_door.show(treasure_door.sample_state_3qubits(1000000))
# End counts for treasure door--------------------------------------------------------------------------------
# Start Monty Hall--------------------------------------------------------------------------------------------
    ry_gate = ry_gate_function(RY_GATE_ANGLE_MONTY_HALL)
    i_ry_gate = tensorProductOnDoors(i_gate, ry_gate)
    hc__i_ry_circuit = normalProductOnDoors(hc_gate, i_ry_gate)
    monty_hall = QuantumOperations(np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
    # Tensored gates (prepared for first part) to apply on initial state
    i_hc__i_ry_gate = tensorProductOnDoors(i_gate, hc__i_ry_circuit)
    xc_i_gate = tensorProductOnDoors(xc_gate, i_gate)
    i_xc_gate = tensorProductOnDoors(i_gate, xc_gate)
    i_i_x_gate = tensorProductOnDoors(i_gate, tensorProductOnDoors(i_gate, x_gate))
    # Monter la première partie du circuit sur quatre qubits
    monty_hall_first_circuit = normalProductOnDoors(normalProductOnDoors(normalProductOnDoors(i_i_x_gate,\
                                        i_xc_gate), xc_i_gate), i_hc__i_ry_gate)
    # Monter monty_hall sur 4 qubits
    monty_hall_first_circuit_on_4qubits = tensorProductOnDoors(i_gate, monty_hall_first_circuit)
    print(monty_hall.normalProductOnSelfAsCircuit1(monty_hall_first_circuit_on_4qubits))
    # Le programme est bon jusqu'a ici
#----------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------
    
    
    
    
    
    # # print(monty_hall_init_state.normalProductOnSelfAsCircuit1(monty_hall_first_circuit))
    # # monty_hall_first_part.init_state = monty_hall_first_part.normalProductOnSelfAsCircuit1(tensored_i_with_hc__i_ry_gate_monty)
    # # monty_hall_first_part.init_state = monty_hall_first_part.normalProductOnSelfAsCircuit1(xc_i_gate)
    # # monty_hall_first_part.init_state = monty_hall_first_part.normalProductOnSelfAsCircuit1(i_xc_gate)
    # # monty_hall_first_part.init_state = monty_hall_first_part.normalProductOnSelfAsCircuit1(i_i_x_gate)
    # # monty_hall_first_part.show(monty_hall_first_part.sample_state_3qubits(100))
    # # # Deuxieme partie de monty hall
    # # monty_hall_init_second_part = QuantumOperations(monty_hall_first_part.init_state)
    # # # print(monty_hall_init_second_part.init_state)
    # # # monty_hall_init_second_part.show(monty_hall_init_second_part.sample_state_3qubits(100))
    
    # # print(monty_hall_first_circuit_on_4qubits)
    # # monty_hall.init_state = monty_hall.normalProductOnSelfAsCircuit1(monty_hall_first_circuit_on_4qubits)
    # # monty_hall.show(monty_hall.sample_state_3qubits(1000000))
    # # print(monty_hall_second_part_on_4qubits.init_state)
    # # print(monty_hall_second_part_on_4qubits.init_state)
    # # # Obtenir la porte CNOT avec le contrôle sur qubit3 et target sur qubit4
    # tensored_xc_gate_with_i = tensorProductOnDoors(xc_gate, i_gate)
    # tensored_xc_gate_with_i_with_i = tensorProductOnDoors(tensored_xc_gate_with_i, i_gate)
    # # Preparer les etapes pour construire xiic_gate
    # swap_on_3qubit_the_first_and_the_second_qubit_gate = tensorProductOnDoors(i_gate, swap_gate)
    # swap_on_4qubit_the_first_and_the_second_qubit_gate = tensorProductOnDoors(i_gate,\
    #                                                     swap_on_3qubit_the_first_and_the_second_qubit_gate)
    # swap_on_3qubit_the_second_and_the_third_qubit_gate = tensorProductOnDoors(swap_gate, i_gate)
    # swap_on_4qubit_the_second_and_the_third_qubit_gate = tensorProductOnDoors(i_gate,\
    #                                                     swap_on_3qubit_the_second_and_the_third_qubit_gate)
    # # Build xiic_gate
    # xiic_gate_first_step = normalProductOnDoors(swap_on_4qubit_the_first_and_the_second_qubit_gate,\
    #                                              tensored_xc_gate_with_i_with_i)
    # xiic_gate = normalProductOnDoors(swap_on_4qubit_the_first_and_the_second_qubit_gate,\
    #                                             xiic_gate_first_step)
    # # Build hcii_gate
    # hcii_gate_first_step = tensorProductOnDoors(hc_gate, i_gate)
    # hcii_gate = tensorProductOnDoors(hcii_gate_first_step, i_gate)
    # # # print(hcii_gate)
    # # # print(monty_hall_second_part_on_4qubits.init_state)
    # # # Do circuit second part of monty hall circuit
    # # monty_hall_second_part_first_step = QuantumOperations(monty_hall_second_part_on_4qubits.normalProductOnSelfAsCircuit1(xiic_gate))
    # # # print(monty_hall_second_part_first_step.init_state)
    # monty_hall_add_second_circuit_first_part = normalProductOnDoors(xiic_gate, monty_hall_first_circuit_on_4qubits)
    # monty_hall_add_second_circuit_last_part = normalProductOnDoors(hcii_gate,monty_hall_add_second_circuit_first_part)
    # # # monty_hall_second_part_last_step = QuantumOperations(monty_hall_second_part_first_step.normalProductOnSelfAsCircuit1(hcii_gate))
    # # # monty_hall_second_part_last_step.show(monty_hall_second_part_last_step.sample_state_3qubits(100))
    # monty_hall.init_state = normalProductOnDoors(monty_hall_add_second_circuit_first_part, monty_hall.init_state)
    # monty_hall.show(monty_hall.sample_state_3qubits(1000000))