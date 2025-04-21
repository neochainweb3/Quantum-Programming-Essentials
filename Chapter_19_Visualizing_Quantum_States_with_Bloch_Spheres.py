from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_vector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
qc = QuantumCircuit(1)
qc.h(0)  # Put qubit into superposition
backend = Aer.get_backend('statevector_simulator')
job = execute(qc, backend)
result = job.result()
plot_bloch_vector(bloch)