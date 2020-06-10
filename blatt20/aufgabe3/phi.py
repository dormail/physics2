### phi.py start ###

import numpy as np

def phi(R, L, C, omega):
    result = R / L * (1 / omega - omega * L * C)
    result = np.arctan(result)
    return result

### phi.py start ###
