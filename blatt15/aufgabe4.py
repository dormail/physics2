import numpy as np
import matplotlib.pyplot as plt


# berechnet das Potential entlang der z-Achse
# R entspricht dem Kugelradius
# r der z Koordinate
def potential(r,R):
    s = 1 # Ladungsdichte
    #epsilon = 0.000000000008854 # elektrische Feldkonstante
    epsilon = 1

    #return s / (2 * epsilon) * R * (np.sqrt(R**2 / r**2 + 1) - np.sqrt(R**2 - 2 * R / r + 1))

    return s / (2 * epsilon) * (R/r) * (np.sqrt(R**2 + r**2) - np.sqrt(R**2 + r**2 - 2 * r * R))


# Kugelradius R
R = 1

x = np.linspace(-100,100,10000)
y = x.copy()

for i in range(0,len(x)):
    y[i] = potential(x[i],R)

# plotting
# der halbkreis
k = np.linspace(-0.5 * np.pi, 0.5 * np.pi)

plt.plot(R * np.cos(k), R * np.sin(k), color='black')
plt.plot(x, y)

# styling
plt.grid(True)
plt.axis('equal')
plt.ylim(-1.5, 3)
plt.xlim(-5,5)

plt.show()
