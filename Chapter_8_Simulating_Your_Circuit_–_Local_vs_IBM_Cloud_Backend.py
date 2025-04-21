from qiskit import Aer, execute, QuantumCircuit
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend=backend, shots=1000)
result = job.result()
counts = result.get_counts()
print(counts)
from qiskit import IBMQ
IBMQ.save_account('YOUR_API_KEY')
IBMQ.load_account()
print(provider.backends())
backend = provider.get_backend('ibmq_quito')
job = execute(qc, backend=backend, shots=1024)
from qiskit.visualization import plot_histogram
qc.draw('mpl')             # Circuit diagram
plot_histogram(counts)     # Result graph