### plot_phi.py start ###

import numpy as np
import matplotlib.pyplot as plt
from phi import phi
from z import z

R = 1
L = 1
C = 1

omega = np.linspace(0.0001, 20, 10000)
p = omega.copy()
s = omega.copy()

for i in range(0, len(omega)):
    p[i] = phi(R, L, C, omega[i])
    s[i] = z(R, L, C, omega[i])

plt.xlabel('ω')

plt.plot(omega, p)
plt.plot(omega, s)
plt.legend(['Phasenverschibung φ(ω)', 'Amplitudenverhältnis'])

plt.savefig('../aufgabe3.png', dpi=600)

plt.show()

### plot_phi.py end ###
