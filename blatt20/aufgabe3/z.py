### z.py start ###

import numpy as np

def z(R, L, C, omega):
    return (L * R) / np.sqrt( L**2 + R**2 * (1 - omega**2 * L * C)**2)


### z.py end ###
