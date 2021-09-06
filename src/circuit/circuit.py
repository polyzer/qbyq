import typing
import numpy as np
from src.gates.operator import Operator

class QuantumCircuit:
    def __init__(self, qubits_count:int = 1, ancilla_count:int = 0):
        self.qubits_count = qubits_count
        self.ancilla_count = ancilla_count
        self.gates_array = []
        self.result_operator = None 

    def add(self, gate):
        self.gates_array.append(gate)

    def dag(self):
        return None
        