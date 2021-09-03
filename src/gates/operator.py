import numpy as np

class Operator:
    def __init__(self, op=np.matrix([[1, 0], [0,1]]), shape=(2, 2)):
        assert isinstance(op, np.ndarray)
        assert len(op.shape) == 2
        assert op.shape[0] == op.shape[1]
        self.operator = op

    def is_unitary(self, matrix):
        cm = matrix.conj()
        return 0

    def is_hermitian(self, matrix):
        return 0
