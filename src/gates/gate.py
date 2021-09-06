from typing import Iterable
import numpy as np
from src.gates.operator import Operator

class Gate:
    def __init__(self, operator:Iterable, qubits:Iterable):
        self.qubits = qubits
        self.operator = operator