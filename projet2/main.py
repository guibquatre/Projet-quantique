from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import matplotlib.pyplot as plt 
from qiskit.visualization import plot_histogram
from qiskit import Aer, execute

def build_ghz_circuit(number_of_qubits):
    qreg = QuantumRegister(number_of_qubits, "q")
    circuit = QuantumCircuit(qreg)
    circuit.h(qreg[0])
    
    for q in range(1,number_of_qubits):
        circuit.cx(qreg[0],qreg[q])
    
    return circuit

# Algorithme de Deustch
# L’algorithme de Deustch ne fait intervenir que deux qubits. Son implémentation devrait être assez
# simple.
# — Construire les circuits quantiques pour les quatre oracles basés sur les quatre types de fonction.
# — Programmer une fonction qui prend en entrée un nombre de 0 à 3 et qui retourne l’oracle correspon-
# dant sous la forme d’une porte quantique.
# — Construire le circuit quantique pour l’algorithme de Deustch à partir de la porte quantique obtenue
# à l’étape précédente.
# — Exécuter ce circuit et vérifier que les résultats concordent avec l’oracle utilisé.
def circuitPourLesQuatresOracles():
    number_of_qubits = 2
    oracle1_circuit = QuantumCircuit(number_of_qubits)
    oracle2_circuit = QuantumCircuit(number_of_qubits)
    oracle3_circuit = QuantumCircuit(number_of_qubits)
    oracle4_circuit = QuantumCircuit(number_of_qubits)
    

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
