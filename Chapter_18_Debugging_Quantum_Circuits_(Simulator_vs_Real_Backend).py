from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_state_city
qc = QuantumCircuit(1)
qc.h(0)
backend = Aer.get_backend('statevector_simulator')
job = execute(qc, backend)
result = job.result()
state = result.get_statevector()
print(state)
plot_state_city(state)
qc.barrier()
qc.save_statevector()