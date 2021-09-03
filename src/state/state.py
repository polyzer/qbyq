import numpy as np

class QuantumState:
    def __init__(self, vec = np.array, n = 4,):
        self.state = np.array([1, 0, 0, 0])
        if self.is_quantum_state(vec):        
            self.state = vec

    def is_quantum_state(self, vec):
        assert len(vec.shape) == 1
        assert vec.shape[0] % 2 == 0
        
        return True