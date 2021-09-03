import numpy as np
from src.gates.operator import Operator

class Gate:
    def __init__(self, qubits=[0]):
        self.qubits = qubits
        