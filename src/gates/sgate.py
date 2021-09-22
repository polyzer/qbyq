from typing import Iterable
import typing
import pdb
import numpy as np
from .gate import Gate
from src.gates.operator import Operator

class SGate(Gate):
    def __init__(self, qubits:Iterable, controlled:bool = False, parametrized:bool = False):
        operator = np.array([
            [1, 0]
            [0, 1j]
        ])
        super().__init__(operator=operator, qubits=qubits)
