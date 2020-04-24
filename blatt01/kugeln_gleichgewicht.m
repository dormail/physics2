% electromagnetic constant
epsilon0 = 8.85 * 10^-12;
% graviational constant
g = 9.81;


% the two angles t1 and t2
t1 = pi/180;
t2 = pi/179;
% length of the ropes
l = 1;
% weight of one sphere
m = 0.1;

% function for the possible charges of the spheres
% to make writing easier defining variable:
p = sqrt(16 * pi * epsilon0 * 4 * l^2 * (sin(t2/2))^2 * tan(t2/2) *m*g);
discr = sqrt((sin(t2/2))^2 * tan(t2/2) - (sin(t1/2))^2 * tan(t1/2));

% charges
q1 = p/2 + 4*l*sqrt(m*g*pi*epsilon0)*discr;
q2 = p/2 - 4*l*sqrt(m*g*pi*epsilon0)*discr;

disp("Charge of sphere 1:");
disp(q1);
disp("Charge of sphere 2:");
disp(q2);