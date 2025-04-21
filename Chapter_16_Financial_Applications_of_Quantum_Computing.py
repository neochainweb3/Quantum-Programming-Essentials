from qiskit_optimization.applications import PortfolioOptimization
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.algorithms import QAOA
from qiskit.utils import algorithm_globals, QuantumInstance
from qiskit import Aer
backend = Aer.get_backend('qasm_simulator')
result = optimizer.solve(problem)
print("Optimal Portfolio:", result.x)