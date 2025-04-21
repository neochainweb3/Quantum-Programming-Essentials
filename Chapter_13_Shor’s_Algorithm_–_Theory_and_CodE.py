from qiskit.algorithms import Shor
from qiskit.utils import QuantumInstance
from qiskit import Aer
simulator = Aer.get_backend('aer_simulator')
result = shor.factor(N=15)
print("Factors of 15:", result.factors)