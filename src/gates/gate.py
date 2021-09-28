from typing import Iterable
import typing
import pdb
import numpy as np
from src.gates.operator import Operator

class Gate:
    def __init__(self, operator:Iterable, qubits:Iterable, controlled:bool = False, parametrized:bool = False):
        """
        ::self.qubits:: sets list of qubits gate acting on
        ::self.operator:: operator as numpy.ndarray
        ::self.controlled:: is controllable gate?
        ::self.parametrized:: if this gate can have various parameters
        """
        self.qubits = qubits
        self.operator = operator
        self.controlled = controlled
        self.parametrized = parametrized

    def apply(self, state):
        vec = state.get_state()
        st = self.operator @ vec
        state.set_state(st)
        return state

    def expand_by_identicals(self, qubits, all_qubits_count):
        """make kronecker product """
        I_op = np.array([
            [1, 0],
            [0, 1]
        ])
        qubits.sort()
        operator_used = False
        current_operator = I_op.copy()
        for i in range(all_qubits_count-1, -1, -1):
            if i in qubits and operator_used == False:
                operator_used = True
                op = self.operator
            else:
                op = I_op
            current_operator = np.kron(op, current_operator)
        return current_operator

    def make_n_controlled(self, control_qubits_count: int, operator: Operator):
        """returns controlled version of this gate"""
        
        pass