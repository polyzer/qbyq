import numpy as np

class Qubit:
    def __init__(self, init_state: np.ndarray = np.array([0, 1])):
        self.state = init_state
        