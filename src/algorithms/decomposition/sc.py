"""
Cosine-Sine decomposition

@misc{sutton2008computing,
      title={Computing the complete CS decomposition}, 
      author={Brian D. Sutton},
      year={2008},
      eprint={0707.1838},
      archivePrefix={arXiv},
      primaryClass={math.NA}
}
"""

import numpy as np
from scipy.linalg import cossin

def make_cs_decompose(operator, p=None, q=None):
    if not p and not q:
        return cossin(operator)
    else:
        return cossin(operator, p=p, q=q)