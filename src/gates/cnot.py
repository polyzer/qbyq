from typing import Iterable
import typing
import pdb
import numpy as np
from .controlled_gate import ControlledGate
from src.gates.operator import Operator

class CNOTGate(ControlledGate):
    def __init__(self, operator:Iterable, qubits:Iterable, controlled:bool = False, parametrized:bool = False):
        self.operator = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ]
        super().__init__(operator=operator, qubits=qubits)