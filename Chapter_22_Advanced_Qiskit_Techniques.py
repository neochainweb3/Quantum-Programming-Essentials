from qiskit import QuantumCircuit
qc = QuantumCircuit(2)
qc.append(sub_qc.to_gate(label='MyGate'), [0, 1])
qc.append(my_instr, [0, 1])
from qiskit import transpile
from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import Unroller
from qiskit_ibm_runtime import QiskitRuntimeService
job = service.run(program_id="circuit-runner", inputs={"circuits": qc})
from qiskit import pulse
from qiskit.pulse import Play, Schedule, DriveChannel, Gaussian