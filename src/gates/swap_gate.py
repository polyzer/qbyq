from typing import Iterable
import typing
import pdb
import numpy as np
from .gate import Gate
from src.gates.operator import Operator

class SwapGate(Gate):
    def __init__(self, operator:Iterable, qubits:Iterable, controlled:bool = False, parametrized:bool = False):
        self.operator = [
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
        ]
        super().__init__(operator=operator, qubits=qubits)