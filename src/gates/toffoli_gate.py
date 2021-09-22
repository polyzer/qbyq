from typing import Iterable
import typing
import pdb
import numpy as np
from .gate import Gate
from src.gates.operator import Operator


class ToffoliGate:
    def __init__(self, operator:Iterable, qubits:Iterable, controlled:bool = False, parametrized:bool = False):
        self.qubits = qubits
        self.operator = operator
        self.controlled = controlled
        self.parametrized = parametrized
