# plot fuer aufgabe 5b 
# die spannung
import numpy as np
import matplotlib.pyplot as plt

def U(t):
    return 10.8 + 3.2 * np.exp(-2 * 0.001 * t/ 3 * 10**4)

t = np.linspace(0,2, 1000)
u = t.copy()

for i in range(len(u)):
    u[i] = U(t[i])

plt.plot(t,u)

plt.ylabel('U in V')
plt.xlabel('t in ms')
plt.legend(['U(t)'])

plt.savefig('aufgabe5b_U.png', dpi=600)
plt.show()
