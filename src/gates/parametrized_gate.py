from typing import Iterable
import typing
import numpy as np
from src.gates.operator import Operator

class Gate:
    def __init__(self, operator:Iterable, qubits:Iterable, controlled:bool = False):
        self.qubits = qubits
        self.operator = operator
        self.controlled = controlled
        self.parametrized = False

    def get_operator(self):
        return self.operator

    def make_controlled(self, control_qubits_count: int):
        """returns controlled version of this gate"""

        pass