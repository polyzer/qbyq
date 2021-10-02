import numpy as np

class QuantumState:
    def __init__(self, qubits_count:int = 2, vec:np.ndarray = np.array([1.+ 0.j, 0.j, 0.j, 0.j]),):
        self.state = vec
        if self.is_quantum_state(vec):        
            self.state = vec
    
    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state

    def __repr__(self):
        return str(self.state)

    def __str__(self):
        return str(self.state)

    def density_matrix(self):
        np.outer(self.state, self.state)

    def is_quantum_state(self, vec):
        assert len(vec.shape) == 1
        assert vec.shape[0] % 2 == 0        
        return True