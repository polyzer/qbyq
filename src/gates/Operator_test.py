import pytest
import numpy
from .operator import Operator
from scipy.stats import unitary_group

def test_unitarity():
    u = unitary_group.rvs(3)
    return Operator.is_unitary(u)

def test_hermitian():
    u = unitary_group.rvs(3)
    return Operator.is_hermitian(u)
