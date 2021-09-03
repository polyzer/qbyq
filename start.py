from src.circuit.circuit import QC
from src.gates import pauli
from src.algorithms.sc import make_cs_decompose
import numpy as np
from scipy.stats import unitary_group

x = unitary_group.rvs(8)

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
print(make_cs_decompose(operator, 4, 4))