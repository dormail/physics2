import matplotlib.pyplot as plt
import numpy as np

# plotet eine kugel mit radius R
def plot_kugel(R):
    t = np.linspace(0,2 * np.pi)
    plt.plot(R * np.cos(t), R * np.sin(t), color='black')

# potential der geladenen Kugel mit Radius R im Abstand r
def potential(r,R):
    eps = 1
    rho = 1
    if r > R:
        return rho * R**3 / (3 * eps * r)
    if r <= R:
        return -1 * rho * r**2 / (6 * eps) + rho * R**2 / (2 * eps)

# efeld, analog zu potential
def efeld(r,R):
    eps = 1
    rho = 1
    if r > R:
        return rho * R**3 / (3 * eps * r**2)
    if r <= R:
        return rho * r / (3 * eps)

R = 1
r = np.linspace(0, 10, 1000)

phi = r.copy()
e = r.copy()

for i in range(0, len(r)):
    phi[i] = potential(r[i], R)
    e[i] = efeld(r[i], R)


plot_kugel(R)
plt.plot(r,phi)
plt.plot(r,e)

plt.xlabel('Distanz r')

plt.axis('equal')
plt.legend(['Geladene Kugel', 'Elektrisches Potential φ(r)', 'Betrag des elektrischen Feldes E(r)'])
plt.savefig('aufgabe2.png', dpi=600)
plt.show()
