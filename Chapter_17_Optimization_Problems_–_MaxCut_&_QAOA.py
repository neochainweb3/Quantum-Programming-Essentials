import networkx as nx
from qiskit_optimization.applications import Maxcut
from qiskit.algorithms import QAOA
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit import Aer
from qiskit.utils import QuantumInstance
backend = Aer.get_backend('qasm_simulator')
result = optimizer.solve(qp)
print("MaxCut solution:", result.x)