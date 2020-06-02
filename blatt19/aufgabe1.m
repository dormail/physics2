% skript um Berechnungen bei Aufgabe 1 urchzufuehren
format short e;
% a)
Uk = 8 * 10^3; % kondensatorspannung
d = 4 * 10^-3; % distanz zwischen kondensator platten
B = 10^-2; % magnetisches Feld beim Kondensator

v = Uk / (d * B); % geschwindigkeit der Teilchen
disp(v); 

% b)
q = 1.6 * 10^-19; % elementarladung als ladung eines Teilchens
l = 1.6; % distanz kondensator <-> fotoplatte
a = 4.5 * 10^-3; % auslenkung an der fotoplatte

% berechnung des auslenkungswinkel
alpha = atan(4.5/1.6 * 10^-3);

m = q * B * l / (v * alpha); % masse eines Teilchens

disp(m);
