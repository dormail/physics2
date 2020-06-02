# plottet den weg des Teilchens bei aufgabe 3

import numpy as np
import matplotlib.pyplot as plt

# geschwindigkeit in v und x richtung
def x(t):
    return vxo * np.sin(omega * t) + 

def y(t):
    return ((E / B + vx0) * (1 / omega) * np.cos(omega * t))

# konstanten
E = -1 # E-Feld
B = 1 # B-Feld (z Richtung)
q = 1 # Ladung des Teilchens
m = 1 # masse des Teilchens

# Randbedingungen (anfangsgeschwindigkeiten)
vx0 = 1
vy0 = 0 

# zyklotronfrequenz
omega = q * B / m
