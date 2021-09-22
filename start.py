from src.circuit.circuit import QuantumCircuit
from src.state.state import QuantumState
from src import gates
from src.algorithms.decomposition.sc import make_cs_decompose
import numpy as np
from scipy.stats import unitary_group

operator = np.array([
    [1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,-1,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,-1,0],
    [0,0,0,0,0,0,0,1],
],)
# print(make_cs_decompose(operator, 4, 4))

qs = QuantumState(vec=np.array([0, 1, 0, 1]))
cnot_operator = np.array([
    [1, 0, 0, 0,],
    [0, 1, 0, 0,],
    [0, 0, 0, 1,],
    [0, 0, 1, 0,],
])
gate = gates.Gate(operator = cnot_operator, qubits=[0,1])
gate = gates.Gate(operator = cnot_operator, qubits=[0,1])
qc = QuantumCircuit(qubits_count=2)
qc.append(gate)

print(qs)
qc.execute(qs)
print(qs)
