from qiskit import QuantumCircuit, Aer, execute
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, backend=simulator, shots=1000)
result = job.result()
counts = result.get_counts(qc)
print("Measurement Results:", counts)
qc.h(0): Applies a Hadamard gate, putting the qubit into a 50/50 superposition
qc.measure(0, 0): Collapses the state into either 0 or 1
result.get_counts(): Tallies how many times 0 and 1 occurred
qc.draw('mpl')  # Requires qiskit[visualization]
from qiskit.visualization import plot_histogram
plot_histogram(counts)