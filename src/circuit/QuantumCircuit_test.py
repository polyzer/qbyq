from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute
from qiskit import IBMQ, Aer

qr = QuantumRegister(4)
qc = QuantumCircuit(qr)

qc.cx(1,0)

unitary_backend = Aer.get_backend('unitary_simulator')
unitary = execute(qc, unitary_backend).result().get_unitary()
print(unitary)