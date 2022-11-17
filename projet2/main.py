from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import matplotlib.pyplot as plt 
from qiskit.visualization import plot_histogram
from qiskit import Aer, execute
from qiskit.tools.visualization import plot_bloch_multivector
# plot_bloch_multivector(statevec)
    # statevec = result.get_statevector()

# from qiskit import IBMQ
# from qiskit.provider.ibmq import least_busy
# token = "..."
# IBMQ.save_account(token)
# IBMQ.load_account()
# IBMQ.get_provider()
# provider.backends, faire une boucle
# def filter_fct(x):
#     return not x.configuration().simulator

# for backend in provider.backends(filters = lambda x: not x.configuration().simulator):
#     print(backend)
# for backend in provider.backends(filters = filter_fct):
#     print(backend)
# backend = least_busy(provider.backends(filters = lambda x: not x.configuration().simulator))

# provider.get_backend("...")

# from qiskit.tools import job_monitor
# job = execute.(..., backend, shots = 1000)
# job_monitor(job)
import sys
from functools import wraps

# def build_ghz_circuit(number_of_qubits):
#     qreg = QuantumRegister(number_of_qubits, "q")
#     circuit = QuantumCircuit(qreg)
#     circuit.h(qreg[0])
    
#     for q in range(1,number_of_qubits):
#         circuit.cx(qreg[0],qreg[q])
    
#     return circuit

def number_between_0_and_3_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not isinstance(args[0], int) or args[0] < 0 or args[0] > 3:
            print("utilisez un nombre en 0 et 3")
            print(f)
            sys.exit(1)
        return f(*args, **kwargs)
    return decorated

def number_over_0_is_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not isinstance(args[1], int) or args[1] < 1:
            print("utilisez un nombre plus haut que zero")
            print(f)
            sys.exit(1)
        return f(*args, **kwargs)
    return decorated

def number_between_1_and_0_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not isinstance(args[0], int) or (args[0] != 1 and args[0] != 0):
            print("utilisez 0 ou 1")
            print(f)
            sys.exit(1)
        return f(*args, **kwargs)
    return decorated

# — Programmer une fonction qui prend en entrée un nombre de 0 à 3 et qui retourne l’oracle 
#   correspondant sous la forme d’une porte quantique.
@number_between_0_and_3_required
def choisirOracleDeDeustch(oracleNumber: int): # -> QuantumCircuit Gate
    number_of_qubits = 2
    gateToReturn = None
    deustchOracle = QuantumCircuit(number_of_qubits)

    # Construire les circuits quantiques pour les quatre oracles basés sur les quatre types de fonction.
    #           x       qubit0 qubit1
    # f0                0      0
    # f1                0      1
    # f2        f(x)    1      0
    # f3                1      1

#   f0 |0⟩ |0⟩ = |0 ⊕ f (0)⟩ |0⟩ = |0 ⊕ 0⟩ |0⟩ = |0⟩ |0⟩
#   f0 |0⟩ |1⟩ = |0 ⊕ f (1)⟩ |1⟩ = |0 ⊕ 0⟩ |1⟩ = |0⟩ |1⟩
#   f0 |1⟩ |0⟩ = |1 ⊕ f (0)⟩ |0⟩ = |1 ⊕ 0⟩ |0⟩ = |1⟩ |0⟩
#   f0 |1⟩ |1⟩ = |1 ⊕ f (1)⟩ |1⟩ = |1 ⊕ 0⟩ |1⟩ = |1⟩ |1⟩ 
    
    if oracleNumber == 0:
        deustchOracle.i(0) # Ne rien faire en faisant quelque chose
        deustchOracle.i(1) 
        gateToReturn = deustchOracle.to_gate(label = "oracle0")

#   f1 |0⟩ |0⟩ = |0 ⊕ f (0)⟩ |0⟩ = |0 ⊕ 0⟩ |0⟩ = |0⟩ |0⟩
#   f1 |0⟩ |1⟩ = |0 ⊕ f (1)⟩ |1⟩ = |0 ⊕ 1⟩ |1⟩ = |1⟩ |1⟩
#   f1 |1⟩ |0⟩ = |1 ⊕ f (0)⟩ |0⟩ = |1 ⊕ 0⟩ |0⟩ = |1⟩ |0⟩
#   f1 |1⟩ |1⟩ = |1 ⊕ f (1)⟩ |1⟩ = |1 ⊕ 1⟩ |1⟩ = |0⟩ |1⟩
    
    elif oracleNumber == 1:
        deustchOracle = QuantumCircuit(number_of_qubits)
        deustchOracle.cx(0,1)
        gateToReturn = deustchOracle.to_gate(label = "oracle1")

#   f2 |0⟩ |0⟩ = |0 ⊕ f (0)⟩ |0⟩ = |0 ⊕ 1⟩ |0⟩ = |1⟩ |0⟩
#   f2 |0⟩ |1⟩ = |0 ⊕ f (1)⟩ |1⟩ = |0 ⊕ 0⟩ |1⟩ = |0⟩ |1⟩
#   f2 |1⟩ |0⟩ = |1 ⊕ f (0)⟩ |0⟩ = |1 ⊕ 1⟩ |0⟩ = |0⟩ |0⟩
#   f2 |1⟩ |1⟩ = |1 ⊕ f (1)⟩ |1⟩ = |1 ⊕ 0⟩ |1⟩ = |1⟩ |1⟩ 

    elif oracleNumber == 2:
        deustchOracle.x(0)
        deustchOracle.cx(0,1)
        deustchOracle.x(0)
        gateToReturn = deustchOracle.to_gate(label = "oracle2")

#   f3 |0⟩ |0⟩ = |0 ⊕ f (0)⟩ |0⟩ = |0 ⊕ 1⟩ |0⟩ = |1⟩ |0⟩
#   f3 |0⟩ |1⟩ = |0 ⊕ f (1)⟩ |1⟩ = |0 ⊕ 1⟩ |1⟩ = |1⟩ |1⟩
#   f3 |1⟩ |0⟩ = |1 ⊕ f (0)⟩ |0⟩ = |1 ⊕ 1⟩ |0⟩ = |0⟩ |0⟩
#   f3 |1⟩ |1⟩ = |1 ⊕ f (1)⟩ |1⟩ = |1 ⊕ 1⟩ |1⟩ = |0⟩ |1⟩

    elif oracleNumber == 3:
        deustchOracle.x(1)
        gateToReturn = deustchOracle.to_gate(label = "oracle3")
    else:
        print("problème avec le décorateur number_between_0_and_3_required")
        sys.exit()

    return gateToReturn
    
    
    # — Construire le circuit quantique pour l’algorithme de Deustch à partir de la porte quantique obtenue
    # à l’étape précédente.
# Une porte quantique à deux qubits, (un oracle) est attendue comme argument 
# Le circuit quantique de deustch est attendu comme retour
def DeustchAlgo(oracleGate):
    number_of_qubits = 2
    deustchCircuit = QuantumCircuit(number_of_qubits)
    deustchCircuit.x(1)
    deustchCircuit.h(1)
    deustchCircuit.h(0)
    deustchCircuit.append(oracleGate, [0,1]) # inverser l'oracle?
    deustchCircuit.h(0)
    return deustchCircuit
    # — Exécuter ce circuit et vérifier que les résultats concordent avec l’oracle utilisé.






















@number_between_1_and_0_required
def deustch_Jozsa_Oracle_const_useCase(_oracleNumber :int, _indexQubits: int, # -> deustch_Jozsa_Oracle_door
                                        _last_Qubit_To_Loop: int, _go_to_real_last_qubit: int,
                                        deustch_Jozsa_Oracle_circuit: QuantumCircuit): 
    while _indexQubits < _last_Qubit_To_Loop:
        deustch_Jozsa_Oracle_circuit.i(_last_Qubit_To_Loop) # ne rien faire en faisant quelque chose
    if _oracleNumber == 0: # f = 0, constante
        deustch_Jozsa_Oracle_circuit.i(_last_Qubit_To_Loop + _go_to_real_last_qubit)
    elif _oracleNumber == 1: # f = 1, constante
        deustch_Jozsa_Oracle_circuit.x(_last_Qubit_To_Loop + _go_to_real_last_qubit)
    return deustch_Jozsa_Oracle_circuit.to_gate(label = "oracle1")
            
@number_between_0_and_3_required
@number_over_0_is_required
def deustch_Jozsa_Oracle(oracleNumber: int, number_of_qubits: int): # -> deustch_Jozsa_Oracle_door
    gate_To_Return = None 
    deustch_Jozsa_Oracle_circuit = QuantumCircuit(number_of_qubits)
    indexQubits = 0
    firstQubit = 0
    operand_substract_to_just_one_before_last_index = 2
    go_to_real_last_qubit = 1
    last_Qubit_To_Loop = number_of_qubits - operand_substract_to_just_one_before_last_index

# — Trouver la forme des circuits quantiques pour les oracles qui implémentent des fonctions constantes
# (il y en a 2). Votre réponse devrait pouvoir s’appliquer à un nombre arbitraire de qubits. 
    if oracleNumber == 0 or oracleNumber == 1: # f = 0, constante
        gate_To_Return = deustch_Jozsa_Oracle_const_useCase(oracleNumber, indexQubits, 
                                                            last_Qubit_To_Loop, go_to_real_last_qubit,
                                                            deustch_Jozsa_Oracle_circuit)
# — Trouver au moins deux circuits quantiques pour les oracles qui implémentent des fonctions balancées.
# Votre réponse devrait pouvoir s’appliquer à un nombre arbitraire de qubits.
    elif oracleNumber == 2 or oracleNumber == 3:
        indexQubits = 1
        while indexQubits < last_Qubit_To_Loop:
            deustch_Jozsa_Oracle_circuit.i(last_Qubit_To_Loop) # ne rien faire en faisant quelque chose
        if oracleNumber == 2:  # f est balancée, version originale
            deustch_Jozsa_Oracle_circuit.cx(firstQubit, number_of_qubits - go_to_real_last_qubit)
        elif oracleNumber == 3: # f est balancée, version not
            deustch_Jozsa_Oracle_circuit.x(firstQubit)
            deustch_Jozsa_Oracle_circuit.cx(firstQubit, number_of_qubits - go_to_real_last_qubit)
            deustch_Jozsa_Oracle_circuit.x(firstQubit)
    
    return gate_To_Return










# — Programmer des fonctions qui prenne en entrée un nombre de qubits retournent ces oracles sous la
# forme de portes quantiques à n qubits.
# — Programmer une fonction qui construit le circuit quantique pour l’algorithme de Deustch-Jozsa à
# partir d’une porte quantique obtenue à l’étape précédente.
# — Exécuter ce circuit et vérifier que les résultats concordent avec l’oracle utilisé.















if __name__== "__main__":e indexQubits < last_Qubit = 0
    # Deustch Start ----------------------------------------------
    while indexQubits < last_Qubit < 4:
        qreg = QuantumRegister(2, "q")
        creg = ClassicalRegister(1, "c")
        deustch = QuantumCircuit(qreg, creg)
        deustch.append(DeustchAlgo(choisirOracleDeDeustce indexQubits < last_Qubit)), [0,1])
        deustch.measure(0, 0)
        qasm_simulator = Aer.get_backend("qasm_simulator")
        jobDeustch = execute(deustch, qasm_simulator, shots = 1000)
        countsDeustch = jobDeustch.result().get_counts()
        plot_histogram(countsDeustch, title="Oracle"+ste indexQubits < last_Qubit))
        print(deustch.decompose())
        print(countsDeustch)
        plt.show()
e indexQubits < last_Qubit += 1
    # Deustch End -------------------------------------------------


#-------------------------------------------------------------------------------------------------
   
    # qreg = QuantumRegister(4, "q")
    # creg = ClassicalRegister(4, "c")
    # circuit = QuantumCircuit(qreg,creg)

    # circuit.h(qreg[0])
    # circuit.cx(qreg[0],qreg[1])
    # circuit.cx(qreg[0],qreg[2])
    # circuit.cx(qreg[0],qreg[3])

    # circuit.barrier()

    # circuit.measure(qreg[0],creg[0])
    # circuit.measure(qreg[1],creg[1])
    # circuit.measure(qreg[2],creg[2])
    # circuit.measure(qreg[3],creg[3])

#--------------------------------------------------------------------------------------------------

    # qreg = QuantumRegister(4, "q")

    # circuit = QuantumCircuit(qreg)

    # circuit.h(qreg[0])
    # circuit.cx(qreg[0],qreg[1])
    # circuit.cx(qreg[0],qreg[2])
    # circuit.cx(qreg[0],qreg[3])
    
    # circuit.measure_all()

#------------------------------------------------------------------------------------------

    # qreg = QuantumRegister(4, "q")
    # circuit = QuantumCircuit(qreg)
    # circuit.h(qreg[0])
    # for q in range(1,4):
    #     circuit.cx(qreg[0],qreg[q])

#------------------------------------------------------------------------------------------

    # circuit = build_ghz_circuit(4)

#------------------------------------------------------------------------------------------

    # number_of_qubits = 4
    # circuit = QuantumCircuit(number_of_qubits)
    # circuit.h(0)
    # for q in range(1,number_of_qubits):
    #     circuit.cx(0,q)

    # circuit.draw(output="mpl")
    # plt.show()

    # fig = circuit.draw(output="mpl")
    # fig.savefig("circuit_ghz_0.pdf")

#------------------------------------------------------------------------------------------

    # number_of_qubits = 4
    # ghz_gate_circuit = QuantumCircuit(number_of_qubits)
    # ghz_gate_circuit.h(0)
    # for q in range(1,number_of_qubits):
    #     ghz_gate_circuit.cx(0,q)

    # ghz_gate = ghz_gate_circuit.to_gate(label = "ghz 4")

    # circuit = QuantumCircuit(number_of_qubits)
    # circuit.x([1,2])
    # circuit.append(ghz_gate,[0,1,2,3])
    # circuit.measure_all()
    # circuit.draw("mpl")
    # # plt.show()

    # qasm_simulator = Aer.get_backend("qasm_simulator")
    # # D'autres argument sont optionnels
    # job = execute(circuit, qasm_simulator, shots = 1000)
    # countsDeustch = job.result().get_counts()
    # print(countsDeustch)

    # plot_histogram(countsDeustch)
    # plt.show()

#--------------------------------------------------------------------------------------------
