from typing import Iterable
import typing
import pdb
import numpy as np
from .controlled_gate import ControlledGate
from src.gates.operator import Operator

class CNOTGate(ControlledGate):
    def __init__(self, control_qubits: Iterable, qubits:Iterable):
        operator = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ])
        super().__init__(operator=operator, control_qubits=control_qubits, qubits=qubits)