qc.ry(data_value, qubit)
qc.rx(θ1, 0)
qc.ry(θ2, 1)
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit_machine_learning.algorithms import VQC
from qiskit_machine_learning.kernels import FidelityQuantumKernel
from qiskit.utils import algorithm_globals
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
qc = QuantumCircuit(2)
qc.h(0)
qc.ry(θ, 1)
qc.cx(0, 1)