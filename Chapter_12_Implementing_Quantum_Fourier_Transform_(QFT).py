from qiskit import QuantumCircuit
from numpy import pi
qc.h(n)
qc.cp(pi / 2**(n - qubit), qubit, n)
qc.swap(i, n - i - 1)
qc = QuantumCircuit(n)
qc.name = "QFT"
qc = qft(3)
qc.draw('mpl')
from qiskit import Aer, execute
backend = Aer.get_backend('statevector_simulator')
job = execute(qc, backend)
result = job.result()
output_state = result.get_statevector()
print(output_state)