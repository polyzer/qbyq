import numpy
from .operator import Operator
from scipy.stats import unitary_group
import pytest

def test_unitarity():
    u = unitary_group.rvs(3)
    Operator.is_unitary(u)
    
def test_hermitian():
    u = unitary_group.rvs(3)
    Operator.is_hermitian(u)

# if __name__ == '__main__':
#     unittest.main()