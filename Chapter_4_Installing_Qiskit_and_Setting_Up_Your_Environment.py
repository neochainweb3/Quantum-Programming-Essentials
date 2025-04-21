from qiskit import QuantumCircuit
qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()
qc.draw()
from qiskit import QuantumCircuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
print(qc)
from qiskit import IBMQ
IBMQ.save_account('YOUR_API_TOKEN')
IBMQ.load_account()
print(provider.backends())