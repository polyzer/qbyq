from typing import Iterable
import typing
import pdb
import numpy as np
from .gate import Gate
from .swap_gate import SwapGate
from src.gates.operator import Operator

class ControlledGate(Gate):
    def __init__(self, operator:Iterable, qubits:Iterable, controlled:bool = False, parametrized:bool = False):
        super().__init__(operator=operator, qubits=qubits)
        
    def make_adjacent_control(self, control_qubits:Iterable, operator_qubits:Iterable, operator: Operator, gate_index: int, gates_array: Iterable) -> Operator:
        """
        ::control_qubits:: - list of qubits that will control
        ::operator_qubits:: - list of qubits that will be affected by operator
        """
        #sort qubits
        control_qubits.sort()
        operator_qubits.sort()
        upper_operator_qubit = operator_qubits[0]
        left_swaps = []
        right_swaps = []
        # now we add SWAP gates to make
        for i in control_qubits:
            for k in range(i, upper_operator_qubit-1):
                left_swaps.append(SwapGate(k, k+1))
                right_swaps.insert(0, SwapGate(k, k+1))
        # we need to replace this gate with new sequence
        gates_array = gates_array[:gate_index] + [gates_array[gate_index]] + gates_array[gate_index+1:]
        return gates_array

