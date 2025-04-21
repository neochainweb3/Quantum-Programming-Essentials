from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_vector, plot_state_city
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
qc = QuantumCircuit(1)
qc.h(0)  # Superposition
backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
plot_bloch_vector(sv.data, title="Bloch Sphere")
plot_state_city(sv.data, title="State City Plot")
plot_state_city() to check amplitude distribution
plot_bloch_vector() to verify rotation steps
plot_histogram() to see unexpected measurement results