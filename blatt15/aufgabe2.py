import numpy as np
import matplotlib.pyplot as plt

# plotet eine kugel mit radius R
def plot_kugel(R):
    t = np.linspace(0,2 * np.pi)
    plt.plot(R * np.cos(t), R * np.sin(t), color='black')

# die gibt da potential im abstand r zurueck
def potential(r,R):
    eps = 1 # elektrische feldkonstante
    rho = 1 # Ladungsdichte

    beta = rho * R**3 / (3 * eps)
    gamma = R**2 * rho  / (2 * eps)
    
    if r <= R:
        return (-1 * rho * r**2 / (6 * eps) + gamma)
    else:
        return (beta / r)

# die analytische ableitung vom potential
def potential_derived(r,R):
    eps = 1 # elektrische feldkonstante
    rho = 1 # Ladungsdichte

    beta = rho * R**3 / (3 * eps)
    gamma = R**2 * rho  / (2 * eps)
    
    if r <= R:
        return -1 * rho * r / (3 * eps)
    else:
        return -1 * beta / (r**2)

# bildet die ableitung von y zu x
def derive(x,y):
    der = y.copy()
    # fuer zentralen werte zentralen diff. quotient
    for i in range(1,len(y) - 1):
        der[i] = (y[i + 1] - y[i - 1]) / (x[i + 1] - x[i - 1])
    # fuer raender normalen difquotien
    der[0] = (y[1] - y[0]) / (x[1] - x[0])
    der[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])
    return der

R = 1
r = np.linspace(0,10) # die werte der x-Achse
phi = r.copy() # das Potential zu den Abstaenden
phi_der = r.copy() # analytisch bestimmte ableitung vom potential
for i in range(0,len(r)):
    phi[i] = potential(r[i], R)
    phi_der[i] = potential_derived(r[i],R)

der = derive(r,phi.copy())


plot_kugel(R)

plt.plot(r,phi) # plot potential
#plt.plot(r, - 1 * der) # plot 1. ableitung 
plt.plot(r, -1 * phi_der) # plot 1. ableitung analytisch

plt.xlabel('Distanz r')

# legende fuer numerischen plot
#plt.legend(['Geladene Kugel', 'Potential', 'Elektrisches Feld,\nnumerische bestimmt', 'Elektrisches Feld,\nanalytisch bestimmt']) 

# legende fuer rein analyitschen plot
plt.legend(['Geladene Kugel', 'Potential', 'Betrag des elektrischen\nFeldes auf eine Testladung'])
plt.title('Potential und 1. Ableitung vom Potential\n einer geladenen Kugel mit Radius R = ' + str(R))
plt.axis('equal')
plt.grid(True)
plt.ylim(-2,2)
plt.show()
