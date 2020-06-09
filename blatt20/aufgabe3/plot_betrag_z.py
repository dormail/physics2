### plot_betrag_z.py start ###

import numpy as np
import matplotlib.pyplot as plt
from z import z

R = 1
L = 1
C = 1

omega = np.linspace(0.01, 100, 100000)
zbetrag = omega.copy()

for i in range(0, len(omega)):
    zbetrag[i] = z(R, L, C, omega[i])

plt.plot(omega, zbetrag)
plt.show()



### plot_betrag_z.py end ###
