from qiskit import QuantumCircuit, Aer, execute
qc = QuantumCircuit(1, 1)
qc.h(0)               # Put qubit into superposition
qc.measure(0, 0)      # Collapse and store result
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend=backend, shots=1000)
result = job.result()
counts = result.get_counts()
print(counts)
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)              # Entangle the qubits
qc.measure([0,1], [0,1]) # Measure both
from qiskit.visualization import plot_histogram
plot_histogram(counts)