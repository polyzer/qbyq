import numpy as np
from scipy.linalg import cossin

def make_cs_decompose(operator, p=None, q=None):
    if not p and not q:
        return cossin(operator)
    else:
        return cossin(operator, p=p, q=q)