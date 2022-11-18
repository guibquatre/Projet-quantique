from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
from qiskit import Aer, execute
import random
import sys
from functools import wraps


# Sert de variables de base pour les deux derniers algos
class VariablesStructure:
    gate_To_Return = None
    oracle_circuit = None
    bernstain_vazirani_Oracle_circuit = None
    last_Qubit_To_Loop = None
    indexQubits = 0
    firstQubit = 0
    go_to_just_one_before_last_Qubit = 2
    go_to_real_last_qubit = 1

    def __init__(self, number_of_qubits):
        self.oracle_circuit = QuantumCircuit(number_of_qubits)
        self.last_Qubit_To_Loop = number_of_qubits - \
            self.go_to_just_one_before_last_Qubit


# START DECORATORS ------------------------------------------------------------------------------------
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
# END DECORATORS -----------------------------------------------------------------------------------------


# START DEUSTCH ------------------------------------------------------------------------------------------
@number_between_0_and_3_required
def choisirOracleDeDeustch(oracleNumber: int):  # -> Quantum Gate
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
        deustchOracle.i(0)  # Ne rien faire en faisant quelque chose
        deustchOracle.i(1)
        gateToReturn = deustchOracle.to_gate(label="oracle0")

    #   f1 |0⟩ |0⟩ = |0 ⊕ f (0)⟩ |0⟩ = |0 ⊕ 0⟩ |0⟩ = |0⟩ |0⟩
    #   f1 |0⟩ |1⟩ = |0 ⊕ f (1)⟩ |1⟩ = |0 ⊕ 1⟩ |1⟩ = |1⟩ |1⟩
    #   f1 |1⟩ |0⟩ = |1 ⊕ f (0)⟩ |0⟩ = |1 ⊕ 0⟩ |0⟩ = |1⟩ |0⟩
    #   f1 |1⟩ |1⟩ = |1 ⊕ f (1)⟩ |1⟩ = |1 ⊕ 1⟩ |1⟩ = |0⟩ |1⟩

    elif oracleNumber == 1:
        deustchOracle = QuantumCircuit(number_of_qubits)
        deustchOracle.cx(0, 1)
        gateToReturn = deustchOracle.to_gate(label="oracle1")

    #   f2 |0⟩ |0⟩ = |0 ⊕ f (0)⟩ |0⟩ = |0 ⊕ 1⟩ |0⟩ = |1⟩ |0⟩
    #   f2 |0⟩ |1⟩ = |0 ⊕ f (1)⟩ |1⟩ = |0 ⊕ 0⟩ |1⟩ = |0⟩ |1⟩
    #   f2 |1⟩ |0⟩ = |1 ⊕ f (0)⟩ |0⟩ = |1 ⊕ 1⟩ |0⟩ = |0⟩ |0⟩
    #   f2 |1⟩ |1⟩ = |1 ⊕ f (1)⟩ |1⟩ = |1 ⊕ 0⟩ |1⟩ = |1⟩ |1⟩

    elif oracleNumber == 2:
        deustchOracle.x(0)
        deustchOracle.cx(0, 1)
        deustchOracle.x(0)
        gateToReturn = deustchOracle.to_gate(label="oracle2")

    #   f3 |0⟩ |0⟩ = |0 ⊕ f (0)⟩ |0⟩ = |0 ⊕ 1⟩ |0⟩ = |1⟩ |0⟩
    #   f3 |0⟩ |1⟩ = |0 ⊕ f (1)⟩ |1⟩ = |0 ⊕ 1⟩ |1⟩ = |1⟩ |1⟩
    #   f3 |1⟩ |0⟩ = |1 ⊕ f (0)⟩ |0⟩ = |1 ⊕ 1⟩ |0⟩ = |0⟩ |0⟩
    #   f3 |1⟩ |1⟩ = |1 ⊕ f (1)⟩ |1⟩ = |1 ⊕ 1⟩ |1⟩ = |0⟩ |1⟩

    elif oracleNumber == 3:
        deustchOracle.x(1)
        gateToReturn = deustchOracle.to_gate(label="oracle3")
    else:
        print("problème avec le décorateur number_between_0_and_3_required")
        sys.exit()

    return gateToReturn


def DeustchAlgo(oracleGate: QuantumCircuit) -> QuantumCircuit: 
    number_of_qubits = 2
    deustchCircuit = QuantumCircuit(number_of_qubits)
    deustchCircuit.x(1)
    deustchCircuit.h(1)
    deustchCircuit.h(0)
    deustchCircuit.append(oracleGate, [0, 1])
    deustchCircuit.h(0)
    return deustchCircuit
#      ┌───┐     ┌──────────┐┌───┐┌─┐
# q_0: ┤ H ├─────┤0         ├┤ H ├┤M├
#      ├───┤┌───┐│  oracle  │└───┘└╥┘
# q_1: ┤ X ├┤ H ├┤1         ├──────╫─
#      └───┘└───┘└──────────┘      ║
#   c: ════════════════════════════╩═
# END DEUSTCH ---------------------------------------------------------------------------------------------
# START DEUSTCH-JOZSA -----------------------------------------------------------------------------------------
@number_between_1_and_0_required
def deustch_Jozsa_Oracle_const_useCase(_oracleNumber: int, _indexQubits: int,  # -> Quantum Gate
                                       _last_Qubit_To_Loop: int, _go_to_real_last_qubit: int,
                                       oracle_circuit: QuantumCircuit, __number_of_qubits: int):
    while _indexQubits <= _last_Qubit_To_Loop:
        oracle_circuit.i(_last_Qubit_To_Loop) # ne rien faire en faisant quelque chose
        _indexQubits += 1
    if _oracleNumber == 0:  # f = 0, constante
        oracle_circuit.i(__number_of_qubits - _go_to_real_last_qubit) # C'est l'opération importante
    elif _oracleNumber == 1:  # f = 1, constante
        oracle_circuit.x(__number_of_qubits - _go_to_real_last_qubit) # C'est l'opération importante
    return oracle_circuit.to_gate(label="oracle1")


@number_between_0_and_3_required
@number_over_0_is_required
def choisirOracleDeustchJozsa(oracleNumber: int, _number_of_qubits: int): # -> deustch_Jozsa_Oracle_door
    variables = VariablesStructure(_number_of_qubits)
    # Circuits quantiques pour les oracles qui implémentent des fonctions constantes
    if oracleNumber == 0 or oracleNumber == 1:
        variables.gate_To_Return = deustch_Jozsa_Oracle_const_useCase(oracleNumber, variables.indexQubits,
                                                                      variables.last_Qubit_To_Loop, 
                                                                      variables.go_to_real_last_qubit,
                                                                      variables.oracle_circuit,
                                                                      _number_of_qubits)
    # Oracles qui implémentent des fonctions balancées.
    elif oracleNumber == 2 or oracleNumber == 3:
        variables.indexQubits = 1 # Commencer après le premier quBit
        while variables.indexQubits <= variables.last_Qubit_To_Loop:
            variables.oracle_circuit.i(variables.last_Qubit_To_Loop) # ne rien faire en faisant quelque chose
            variables.indexQubits += 1
        if oracleNumber == 2:  # f est balancée, version originale
            variables.oracle_circuit.cx( # C'est l'opération importante
                variables.firstQubit, _number_of_qubits - variables.go_to_real_last_qubit)
            variables.gate_To_Return = variables.oracle_circuit.to_gate(
                label="oracle2")
        elif oracleNumber == 3:  # f est balancée, version not
            variables.oracle_circuit.x(variables.firstQubit) # C'est l'opération importante
            variables.oracle_circuit.cx( # C'est l'opération importante
                variables.firstQubit, _number_of_qubits - variables.go_to_real_last_qubit)
            variables.oracle_circuit.x(variables.firstQubit) # C'est l'opération importante
            variables.gate_To_Return = variables.oracle_circuit.to_gate(
                label="oracle3")

    return variables.gate_To_Return


@number_over_0_is_required
def deustchJozsaAlgo(oracleGate: QuantumCircuit, number_of_qubits: int): # -> Quantum Gate
    variables = VariablesStructure(number_of_qubits)
    while variables.indexQubits <= variables.last_Qubit_To_Loop:
        variables.oracle_circuit.h(variables.indexQubits)
        variables.indexQubits += 1
    variables.oracle_circuit.x(number_of_qubits - variables.go_to_real_last_qubit)
    variables.oracle_circuit.h(number_of_qubits - variables.go_to_real_last_qubit)
    variables.indexQubits = 0
    list_index_to_append = []
    while variables.indexQubits < number_of_qubits:
        list_index_to_append.append(variables.indexQubits)
        variables.indexQubits += 1
    variables.oracle_circuit.append(oracleGate, list_index_to_append)
    variables.indexQubits = 0
    while variables.indexQubits <= variables.last_Qubit_To_Loop:
        variables.oracle_circuit.h(variables.indexQubits)
        variables.indexQubits += 1
    return variables.oracle_circuit.to_gate(label="deustch-jozsa-circuit")
#                ┌───┐     ┌──────────┐┌───┐┌─┐         
# quantumReg2_0: ┤ H ├─────┤0         ├┤ H ├┤M├─────────
#                ├───┤     │          │├───┤└╥┘┌─┐      
# quantumReg2_1: ┤ H ├─────┤1         ├┤ H ├─╫─┤M├──────
#                ├───┤     │          │├───┤ ║ └╥┘┌─┐   
# quantumReg2_2: ┤ H ├─────┤2 oracle1 ├┤ H ├─╫──╫─┤M├───
#                ├───┤     │          │├───┤ ║  ║ └╥┘┌─┐
# quantumReg2_3: ┤ H ├─────┤3         ├┤ H ├─╫──╫──╫─┤M├
#                ├───┤┌───┐│          │└───┘ ║  ║  ║ └╥┘
# quantumReg2_4: ┤ X ├┤ H ├┤4         ├──────╫──╫──╫──╫─
#                └───┘└───┘└──────────┘      ║  ║  ║  ║ 
# classicReg2_0: ════════════════════════════╩══╬══╬══╬═
#                                               ║  ║  ║ 
# classicReg2_1: ═══════════════════════════════╩══╬══╬═
#                                                  ║  ║ 
# classicReg2_2: ══════════════════════════════════╩══╬═
#                                                     ║ 
# classicReg2_3: ═════════════════════════════════════╩═
# END DEUSTCH-JOZSA -----------------------------------------------------------------------------------------
# START ORACLE Bernstein-Vazirani ----------------------------------------------------------------------------
def choisirOracleBernstein_Vazirani(_number_of_qubits: int):
    s = random.randint(1, ((2**(_number_of_qubits-1))-1))
    variables = VariablesStructure(_number_of_qubits)
    binaire = bin(s)[2:]
    print("s: "+str(s))
    print("binaire: "+str(binaire))
    lastQubit = _number_of_qubits - variables.go_to_real_last_qubit
    indexInverse = len(binaire) - 1
    while indexInverse >= 0:
        if (binaire[indexInverse] == "1"): # cherche les qubits à l'état 1
            variables.oracle_circuit.cx(variables.indexQubits, lastQubit)
        variables.indexQubits += 1
        indexInverse -= 1
    print(variables.oracle_circuit.decompose())
    return variables.oracle_circuit.to_gate(label="bernstein-vazirani_ORACLE")
# Base 10: 11
# Base 2:  1011
# (0) 1
# (1) 0
# (2) 1
# (3) 1                
# q_0: ──■────────────
#        │            
# q_1: ──┼────────────
#        │            
# q_2: ──┼────■───────
#        │    │       
# q_3: ──┼────┼────■──
#      ┌─┴─┐┌─┴─┐┌─┴─┐
# q_4: ┤ X ├┤ X ├┤ X ├
#      └───┘└───┘└───┘
# END ORACLE Bernstein-Vazirani ----------------------------------------------------------------------------
if __name__ == "__main__":
    indexOracles = 0
    # # Deustch START ----------------------------------------------------------
    while indexOracles < 4:
        qreg = QuantumRegister(2, "quest1")
        creg = ClassicalRegister(1, "c")
        deustch = QuantumCircuit(qreg, creg)
        deustch.append(DeustchAlgo(
            choisirOracleDeDeustch(indexOracles)), [0, 1])

        deustch.measure(0, 0)
        qasm_simulator = Aer.get_backend("qasm_simulator")
        jobDeustch = execute(deustch, qasm_simulator, shots=1000)
        countsDeustch = jobDeustch.result().get_counts()
        plot_histogram(countsDeustch, title="Deustch_Oracle_Result"+str(indexOracles))
        print(deustch.decompose())
        print(countsDeustch)
        plt.show()
        indexOracles += 1
    # Deustch END --------------------------------------------------------------------
    # Deustch-Jozsa START --------------------------------------------------------------
    indexOracles = 0
    while indexOracles < 4:
        randomNumber = random.randint(2, 2**3) # Maximum choisi arbitrairement
        variables = VariablesStructure(randomNumber)
        lastToMeasure = randomNumber - variables.go_to_just_one_before_last_Qubit
        qreg2 = QuantumRegister(randomNumber, "quantumReg2")
        creg2 = ClassicalRegister(randomNumber - variables.go_to_real_last_qubit, "classicReg2")
        deustch_jozsa = QuantumCircuit(qreg2, creg2)
        _deustchJozsaAlgo = deustchJozsaAlgo(choisirOracleDeustchJozsa(indexOracles, randomNumber), randomNumber)

        # Construire une liste pour l'argument de append(), (patch)
        list_index_to_append = []
        while variables.indexQubits < randomNumber:
            list_index_to_append.append(variables.indexQubits)
            variables.indexQubits += 1

        deustch_jozsa.append(_deustchJozsaAlgo, list_index_to_append)
        
        variables.indexQubits = 0
        while variables.indexQubits <= lastToMeasure:
            deustch_jozsa.measure(variables.indexQubits, variables.indexQubits)
            variables.indexQubits += 1
            
        qasm_simulator = Aer.get_backend("qasm_simulator")
        jobDeustchJozsa = execute(deustch_jozsa, qasm_simulator, shots=1000)
        countsDeustchJozsa = jobDeustchJozsa.result().get_counts()
        plot_histogram(countsDeustchJozsa, title="Deustch-Jozsa_Oracle_Result"+str(indexOracles))
        print(deustch_jozsa.decompose())
        print(countsDeustchJozsa)
        plt.show()
        indexOracles += 1
    # Deustch-Jozsa END --------------------------------------------------------------------------
    # Bernstain-Vazirani START--------------------------------------------------------------------
    randomNumber = random.randint(2, 2**3) # Maximum choisi arbitrairement
    variables = VariablesStructure(randomNumber)
    print("numberOfQuBits: "+str(randomNumber))
    lastToMeasure = randomNumber - variables.go_to_just_one_before_last_Qubit
    qreg2 = QuantumRegister(randomNumber, "quantumReg2")
    creg2 = ClassicalRegister(randomNumber - variables.go_to_real_last_qubit, "classicReg2")
    deustch_jozsa = QuantumCircuit(qreg2, creg2)
    _bernstein_Vazirani = deustchJozsaAlgo(choisirOracleBernstein_Vazirani(randomNumber), randomNumber)

    # Construire une liste pour l'argument de append(), (patch)
    list_index_to_append = []
    while variables.indexQubits < randomNumber:
        list_index_to_append.append(variables.indexQubits)
        variables.indexQubits += 1

    deustch_jozsa.append(_bernstein_Vazirani, list_index_to_append)
    
    variables.indexQubits = 0
    while variables.indexQubits <= lastToMeasure:
        deustch_jozsa.measure(variables.indexQubits, variables.indexQubits)
        variables.indexQubits += 1
        
    qasm_simulator = Aer.get_backend("qasm_simulator")
    jobDeustchJozsa = execute(deustch_jozsa, qasm_simulator, shots=1000)
    countsDeustchJozsa = jobDeustchJozsa.result().get_counts()
    plot_histogram(countsDeustchJozsa, title="Bernstein-Vazirani_Oracle_Result")
    print(deustch_jozsa.decompose())
    print(countsDeustchJozsa)
    plt.show()
    # Bernstain-Vazirani END--------------------------------------------------------------------
