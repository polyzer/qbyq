from typing import Iterable
import typing
import pdb
import numpy as np
from src.gates.operator import Operator

class Gate:
    def __init__(self, operator:Iterable, qubits:Iterable, control_qubits:Iterable=[], controlled:bool = False, parametrized:bool = False):
        """
        ::self.qubits:: sets list of qubits gate acting on
        ::self.operator:: operator as numpy.ndarray
        ::self.controlled:: is controllable gate?
        ::self.parametrized:: if this gate can have various parameters
        """
        self.qubits = qubits
        self.control_qubits = control_qubits
        self.operator = operator
        self.controlled = controlled
        self.parametrized = parametrized

    def apply(self, state):
        vec = state.get_state()
        # pdb.set_trace()
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
        # current_operator = 1
        waiting = 0
        # pdb.set_trace()
        if (all_qubits_count-1 in (self.control_qubits)) or (all_qubits_count-1 in (self.qubits)):
            current_operator = self.operator
            operator_used = True
        else:
            current_operator = I_op

        for i in range(all_qubits_count-2, -1, -1):
            if ((i in qubits) or (i in self.control_qubits)):
                if (operator_used == False):
                    operator_used = True
                    current_operator = np.kron(self.operator, current_operator)
                    print("was kron")
            else:
                current_operator = np.kron(I_op, current_operator)
                print("was kron I")
            print(current_operator)
        pdb.set_trace()
        self.operator = current_operator

    def make_n_controlled(self, control_qubits_count: int, operator: Operator):
        """returns controlled version of this gate"""
        
        pass