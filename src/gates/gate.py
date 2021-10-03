from typing import Iterable
import typing
import pdb
import numpy as np
from src.gates.operator import Operator

class Gate:
    def __init__(self, operator:Iterable, qubits:Iterable, controlled_qubits:Iterable=[], controlled:bool = False, parametrized:bool = False):
        """
        ::self.qubits:: sets list of qubits gate acting on
        ::self.operator:: operator as numpy.ndarray
        ::self.controlled:: is controllable gate?
        ::self.parametrized:: if this gate can have various parameters
        """
        self.qubits = qubits
        self.controlled_qubits = controlled_qubits
        self.operator = operator
        self.controlled = controlled
        self.parametrized = parametrized

    def apply(self, state):
        vec = state.get_state()
        st = self.operator @ vec
        state.set_state(st)
        return state

    def expand_by_identicals(self, circuit_qubits_count):
        """make kronecker product """
        I_op = np.array([
            [1, 0],
            [0, 1]
        ])
        all_qubits_count = circuit_qubits_count
        qubits = self.qubits
        qubits.sort()
        operator_used = False
        current_operator = I_op.copy()
        waiting = 0
        for i in range(all_qubits_count-1, -1, -1):
            if ((i in qubits) or (i in self.controlled_qubits)) and (operator_used == False):
                operator_used = True
                # op = self.operator
                waiting = len(qubits) + len(self.qubits)
                if all_qubits_count-1:
                    current_operator = np.kron(self.operator, current_operator)
                else:
                    current_operator = np.kron(current_operator, self.operator)
            elif waiting:
                waiting -= 1
            else:
                op = I_op
                current_operator = np.kron(op, current_operator)

        pdb.set_trace()
        self.operator = current_operator

    def make_n_controlled(self, control_qubits_count: int, operator: Operator):
        """returns controlled version of this gate"""
        
        pass