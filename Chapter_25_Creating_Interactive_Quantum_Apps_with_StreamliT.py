import streamlit as st
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
qc = QuantumCircuit(qubits, qubits)
qc.h(0)
qc.x(0)
qc.measure_all()
backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend, shots=1024).result()
counts = result.get_counts()