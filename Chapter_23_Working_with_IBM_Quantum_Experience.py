from qiskit import IBMQ
IBMQ.save_account('your-token-here')
IBMQ.load_account()
backends = provider.backends()
backend = provider.get_backend('ibmq_quito')
print(backend.status())
from qiskit import execute
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0,1], [0,1])
job = execute(qc, backend=backend, shots=1024)
result = job.result()
counts = result.get_counts()
print(counts)
from qiskit_ibm_runtime import QiskitRuntimeService
job = service.run(program_id="sampler", inputs={"circuits": [qc]})
print(job.result())