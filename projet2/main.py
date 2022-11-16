from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import matplotlib.pyplot as plt 
from qiskit.visualization import plot_histogram
from qiskit import Aer, execute
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

# S'assurer que l'argument est entre 0 et 3
def number_between_0_and_3_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not isinstance(args[1], int) or args[1] < 0 or args[1] > 3:
            print("utilisez un nombre en 0 et 3 pour circuitPourLesQuatresOraclesDeDeustch()")
            sys.exit(1)
        return f(*args, **kwargs)
    return decorated

# — Programmer une fonction qui prend en entrée un nombre de 0 à 3 et qui retourne l’oracle correspondant sous la forme d’une porte quantique.
@number_between_0_and_3_required
def circuitPourLesQuatresOraclesDeDeustch(oracleNumber: int): # -> QuantumCircuit Gate
    number_of_qubits = 2
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
        deustch0 = QuantumCircuit(number_of_qubits)
        deustch0.i(0) # Ne rien faire en faisant quelque chose
        deustch0.i(0) # Ne rien faire en faisant quelque chose
        deustch0.to_gate(label = "oracle0")

#   f1 |0⟩ |0⟩ = |0 ⊕ f (0)⟩ |0⟩ = |0 ⊕ 0⟩ |0⟩ = |0⟩ |0⟩
#   f1 |0⟩ |1⟩ = |0 ⊕ f (1)⟩ |1⟩ = |0 ⊕ 1⟩ |1⟩ = |1⟩ |1⟩
#   f1 |1⟩ |0⟩ = |1 ⊕ f (0)⟩ |0⟩ = |1 ⊕ 0⟩ |0⟩ = |1⟩ |0⟩
#   f1 |1⟩ |1⟩ = |1 ⊕ f (1)⟩ |1⟩ = |1 ⊕ 1⟩ |1⟩ = |0⟩ |1⟩
    
    elif oracleNumber == 1:
        deustch1 = QuantumCircuit(number_of_qubits)
        deustch1.cx(0,1)
        deustch1.to_gate(label = "oracle1")

#   f2 |0⟩ |0⟩ = |0 ⊕ f (0)⟩ |0⟩ = |0 ⊕ 1⟩ |0⟩ = |1⟩ |0⟩
#   f2 |0⟩ |1⟩ = |0 ⊕ f (1)⟩ |1⟩ = |0 ⊕ 0⟩ |1⟩ = |0⟩ |1⟩
#   f2 |1⟩ |0⟩ = |1 ⊕ f (0)⟩ |0⟩ = |1 ⊕ 1⟩ |0⟩ = |0⟩ |0⟩
#   f2 |1⟩ |1⟩ = |1 ⊕ f (1)⟩ |1⟩ = |1 ⊕ 0⟩ |1⟩ = |1⟩ |1⟩ 

    elif oracleNumber == 2:
        deustch2 = QuantumCircuit(number_of_qubits)
        deustch2.x(0)
        deustch2.cx(0,1)
        deustch2.x(0)
        deustch2.to_gate(label = "oracle2")

#   f3 |0⟩ |0⟩ = |0 ⊕ f (0)⟩ |0⟩ = |0 ⊕ 1⟩ |0⟩ = |1⟩ |0⟩
#   f3 |0⟩ |1⟩ = |0 ⊕ f (1)⟩ |1⟩ = |0 ⊕ 1⟩ |1⟩ = |1⟩ |1⟩
#   f3 |1⟩ |0⟩ = |1 ⊕ f (0)⟩ |0⟩ = |1 ⊕ 1⟩ |0⟩ = |0⟩ |0⟩
#   f3 |1⟩ |1⟩ = |1 ⊕ f (1)⟩ |1⟩ = |1 ⊕ 1⟩ |1⟩ = |0⟩ |1⟩

    elif oracleNumber == 3:
        deustch3 = QuantumCircuit(number_of_qubits)
        deustch3.x(1)
        deustch3.to_gate(label = "oracle3")

    else:
        print("problème avec le décorateur number_between_0_and_3_required")
        sys.exit()




    # — Construire le circuit quantique pour l’algorithme de Deustch à partir de la porte quantique obtenue
    # à l’étape précédente.
    # — Exécuter ce circuit et vérifier que les résultats concordent avec l’oracle utilisé.


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
    # counts = job.result().get_counts()
    # print(counts)

    # plot_histogram(counts)
    # plt.show()


if __name__== "__main__":
    None

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
    # print(ghz_gate.type())

    # circuit = QuantumCircuit(number_of_qubits)
    # circuit.x([1,2])
    # circuit.append(ghz_gate,[0,1,2,3])
    # circuit.measure_all()
    # circuit.draw("mpl")
    # # plt.show()

    # qasm_simulator = Aer.get_backend("qasm_simulator")
    # # D'autres argument sont optionnels
    # job = execute(circuit, qasm_simulator, shots = 1000)
    # counts = job.result().get_counts()
    # print(counts)

    # plot_histogram(counts)
    # plt.show()

#--------------------------------------------------------------------------------------------
