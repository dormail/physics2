# ein skript welches bei aufgabe 3 zahlen einsetzt
import numpy as np

# konstanten
l = 0.03 # kantenlaenge
R = 0.001 # der Widerstand
rho = 2 * 10**4 # dichte von gold
rho_r = 2.2 * 10**(-8) # spezifischer widerstand gold
k = 50630 # goldpreis
pi = np.pi

# berechnung des preises
p = k * rho * 6 * rho_r * l**2 / R

print('Der Wuerfel kostet ' + str(p) + 'Euro')
