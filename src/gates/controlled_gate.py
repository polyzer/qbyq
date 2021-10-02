from typing import Iterable
import typing
import pdb
import numpy as np
from .gate import Gate
from .swap_gate import SwapGate
from src.gates.operator import Operator

class ControlledGate(Gate):
    def __init__(self, operator:Iterable, control_qubits: Iterable, qubits:Iterable, controlled:bool = True, parametrized:bool = False):
        super().__init__(operator=operator, qubits=qubits)
        self.control_qubits = control_qubits

    def make_adjacent_control_gates_array(self) -> Operator:
        """
        ::control_qubits:: - list of qubits that will control
        ::operator_qubits:: - list of qubits that will be affected by operator
        """
        #sort qubits
        #THERE WE NEED TO MAKE WORK!
        self.control_qubits.sort()
        self.qubits.sort()
        upper_operator_qubit = self.qubits[0]
        left_swaps = []
        right_swaps = []
        # now we add SWAP gates to make
        for i in self.control_qubits:
            for k in range(i, upper_operator_qubit-1):
                left_swaps.append(SwapGate(k, k+1))
                right_swaps.insert(0, SwapGate(k, k+1))
        # we need to replace this gate with new sequence
        gates_array = left_swaps + [self] + right_swaps
        return gates_array

