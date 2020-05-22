# plot fuer aufgabe 5b 
# die strom
import numpy as np
import matplotlib.pyplot as plt

def I(t):
    return 0.0432 + (0.031 - 0.0432) * np.exp(-2 * 0.001 * t/ 3 * 10**4)

t = np.linspace(0,2, 1000)
u = t.copy()

for i in range(len(u)):
    u[i] = I(t[i])

plt.plot(t,u)

plt.ylabel('I in A')
plt.xlabel('t in ms')
plt.legend(['I(t)'])

plt.savefig('aufgabe5b_I.png', dpi=600)
plt.show()
