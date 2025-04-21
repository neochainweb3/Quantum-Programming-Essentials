qc.h(0)
qc.x(0)
qc.y(0)
qc.z(0)
qc.cx(control_qubit, target_qubit)
qc.rx(3.14, 0)
qc.rz(1.57, 0)
from qiskit import QuantumCircuit
qc = QuantumCircuit(2, 2)
qc.h(0)       # Superposition
qc.cx(0, 1)   # Entangle
qc.measure([0,1], [0,1])
qc.draw('mpl')