from typing import Iterable
import numpy as np
from src.gates.operator import Operator
from src.gates.controlled_gate import ControlledGate
from src.state.quantum_state import QuantumState
from src.state.qubit import Qubit

class QuantumCircuit:
    def __init__(self, qubits_count:int = 1, ancilla_count:int = 0, parametrized:bool = False):
        self.qubits_count = qubits_count
        self.ancilla_count = ancilla_count
        self.gates_array = []
        self.result_operator = None
        self.qubits = self.create_qubits(qubits_count)

    def make_preprocessing(self, gates_array: Iterable) -> Iterable:
        new_gates_array = []
        for i in range(len(self.gates_array)):
            gate = self.gates_array[i]
            if isinstance(gate, ControlledGate):                
                adj_gates_array = gate.make_adjacent_control_gates_array()
                new_gates_array += adj_gates_array
            else:
                new_gates_array.append(gate)
            return new_gates_array

        return gates_array

    def execute(self, state: QuantumState):
        self.gates_array = self.make_preprocessing(self.gates_array)
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