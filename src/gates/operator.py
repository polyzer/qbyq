import numpy as np

class Operator:
    def __init__(self, operator:np.ndarray =np.array([[1, 0], [0,1]]), shape=(2, 2)):
        assert isinstance(operator, np.ndarray), "Operator must be a np.ndarray"
        assert len(operator.shape) == 2, "Operator shape dimensions must be equal to 2"
        assert operator.shape[0] == operator.shape[1], "Operator must be square"
        self.operator = operator

    @staticmethod
    def is_unitary(matrix):
        shape = matrix.shape
        assert shape[0] == shape[1], "Matrix must be square"   
        id = np.eye(shape[0])
        cm = matrix.conj()
        if (cm @ matrix == id).all() and (matrix @ cm == id).all():
            return True
        else:
            return False

    @staticmethod
    def is_hermitian(matrix):
        shape = matrix.shape
        assert shape[0] == shape[1], "Matrix must be square" 
        cm = matrix.conj()

        if np.equal(cm, matrix).all():
            return True
        else:
            return False
