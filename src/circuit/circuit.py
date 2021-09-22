from typing import Iterable
import numpy as np
from src.gates.operator import Operator
from src.state.state import QuantumState
from src.state.qubit import Qubit

class QuantumCircuit:
    def __init__(self, qubits_count:int = 1, ancilla_count:int = 0, parametrized:bool = False):
        self.qubits_count = qubits_count
        self.ancilla_count = ancilla_count
        self.gates_array = []
        self.result_operator = None
        self.qubits = self.create_qubits(qubits_count)


    # def add_swaps_to_non_neighbor_cnot(self, gates_array: Iterable, gate_index: int) -> Iterable:
    #     """"""
    #     new_gates_set = []
    #     gate = gates_array[gate_index]
    #     qubits = gate.qubits
    #     for i in range(len(qubits)):
    #         q = qubits[i]
            
    #     return

    def execute(self, state: QuantumState):
        for i in range(len(self.gates_array)):
            state = self.gates_array[i].apply(state)
        return state
        
    def create_qubits(self, qubits_count: int) -> list:
        qubits = []
        for i in range(qubits_count):
            qubits.append(Qubit())
        return qubits

    def create_state(self, qubits_count: int) -> QuantumState:
        qs = QuantumState(qubits_count)

    def append(self, gate):
        self.gates_array.append(gate)

    def dag(self):
        return None
        
    def __repr__(self) -> str:
        pass
    
    def __str__(self) -> str:
        pass