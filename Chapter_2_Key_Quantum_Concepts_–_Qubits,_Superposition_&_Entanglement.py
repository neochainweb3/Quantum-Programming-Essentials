from qiskit import QuantumCircuit
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
from qiskit import QuantumCircuit
qc = QuantumCircuit(2, 2)
qc.h(0)          # Superposition
qc.cx(0, 1)      # Entangle
qc.measure([0, 1], [0, 1])