from qiskit import QuantumCircuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc = bell_pair()
qc.measure_all()
from qiskit.circuit import Parameter
qc = QuantumCircuit(1)
qc.ry(θ, 0)
from qiskit import QuantumCircuit
qc = QuantumCircuit(n)
qc.h(0)
qc.cx(i, i + 1)
from quantum_utils.entanglement import create_ghz
qc = create_ghz()