% berechnung der elektrischen ladung der Erde
format long

% konstanten
epsilon0 = 8.8541878128 * 10^(-12); % elektrische feldkonstante
re = 6370000; % radius der erde
E = 150; % elektrisches Feld

sigma = -1 * E * epsilon0;
Q = sigma * 4 * pi * re^2;

disp(sigma);
disp(Q);