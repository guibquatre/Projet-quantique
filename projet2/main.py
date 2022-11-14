from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import matplotlib.pyplot as plt 
from qiskit.visualization import plot_histogram
from qiskit import Aer, execute
import sys
from functools import wraps

def build_ghz_circuit(number_of_qubits):
    qreg = QuantumRegister(number_of_qubits, "q")
    circuit = QuantumCircuit(qreg)
    circuit.h(qreg[0])
    
    for q in range(1,number_of_qubits):
        circuit.cx(qreg[0],qreg[q])
    
    return circuit



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
    oracle0_circuit = QuantumCircuit(number_of_qubits)
    oracle0_circuit.x(1) # ready
    oracle1_circuit = QuantumCircuit(number_of_qubits)
    oracle2_circuit = QuantumCircuit(number_of_qubits) # ready
    oracle3_circuit = QuantumCircuit(number_of_qubits)
    # Construire les circuits quantiques pour les quatre oracles basés sur les quatre types de fonction.
 
    oracle1_circuit.x(0)
    oracle1_circuit.x(1) # ready
    oracle3_circuit.x(0)
    oracle3_circuit.x(1)


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
