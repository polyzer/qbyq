import numpy as np
from src.gates.operator import Operator

class QC:
    def __init__(self, qubits_count=1, ancilla_count=0):
        self.qubits_count = qubits_count
        self.ancilla_count = ancilla_count
        self.gates_array = []

    def add(self, gate):
        self.gates_array.append(gate)

    def dag(self):
        return None
        