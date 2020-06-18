% script um werte bei aufgabe 2 zu berechnen

% aufgabe a)
PH = 1800; % Leistung des Luefters in Watt
UH = 230; % Betriebsspannung in Volt
R = 25; % widerstand in ohm

I = PH / UH % strom der fließt
PR = R * I^2
PG = PR + PH
eta = PH / PG % wirkungsgrad

% aufgabe b)
I_R = I / 9
PRP = R * I_R^2
PGP = PH + PRP
etap = PH / PGP
