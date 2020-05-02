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

# elektrisches potential eines geladenen ringes
# Ring besitzt Radius R
# Abstanz z
def potential_ring(z,R):
    q = 2 * np.pi * R # overall charge of the ring
    return q / np.sqrt(z**2 + R**2)


# numerische berechnung des potentials der kugelschale, aufteilung in ringe
# z ist die z-Koordinate
# R Kugelradius
# p die genauigkeit (menge an ringen)
def potential_halbkugel_num(z, R, p):
    t = np.linspace(0/p, np.pi/2, p) # winkel
    r = R * np.sin(t)
    d = z - R * np.cos(t)
    result = 0
    for i in range(0,len(t)):
        result = result + potential_ring(d[i],r[i])
    result = result
    return result
    

# Kugelradius R
R = 1
p = 1000

x = np.linspace(-10,10,1000)
y = x.copy()
ynum = x.copy()

for i in range(0,len(x)):
    y[i] = potential(x[i],R)
    ynum[i] = potential_halbkugel_num(x[i], R, p)

ynum = ynum / max(ynum)

# plotting
# der halbkreis
k = np.linspace(-0.5 * np.pi, 0.5 * np.pi)

plt.plot(R * np.cos(k), R * np.sin(k), color='black')
plt.plot(x, y)
print(ynum)
plt.plot(x, ynum)

plt.legend(['Kugelschale', 'Potential analytisch', 'Potential numerisch'])

# styling
plt.grid(True)
plt.axis('equal')
plt.ylim(-1.5, 3)
plt.xlim(-5,5)

plt.show()
