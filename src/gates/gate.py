from typing import Iterable
import typing
import pdb
import numpy as np
from src.gates.operator import Operator

class Gate:
    def __init__(self, operator:Iterable, qubits:Iterable, controlled:bool = False, parametrized:bool = False):
        self.qubits = qubits
        self.operator = operator
        self.controlled = controlled
        self.parametrized = parametrized

    def apply(self, state):
        vec = state.get_state()
        st = self.operator @ vec
        state.set_state(st)
        return state

    def expand_by_identical(self):
        for i in self.qubits:
            q = self.qubits[i]

    def make_controlled(self, control_qubits_count: int):
        """returns controlled version of this gate"""

        pass