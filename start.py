from src.circuit.circuit import QuantumCircuit
from src.state.quantum_state import QuantumState
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

qs = QuantumState(vec=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
cnot_operator = np.array([
    [1, 0, 0, 0,],
    [0, 1, 0, 0,],
    [0, 0, 0, 1,],
    [0, 0, 1, 0,],
])
gate = gates.Gate(operator = cnot_operator, qubits=[0,1])
cnotgate = gates.CNOTGate(control_qubits = [1], qubits=[2])
qc = QuantumCircuit(qubits_count=4)
qc.append(cnotgate)
qc.append(gate)

print(qs)
qc.execute(qs)
print(qc.gates_array)
print(qs)
