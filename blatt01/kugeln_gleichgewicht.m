% printing out
theta1 = pi/3;
theta2 = pi/2.5;
disp("Charge of sphere 1:");
disp(charge1(theta1,theta2));
disp("Charge of sphere 2:");
disp(charge2(theta1,theta2));
disp("Note that also the negative pair is a possible solution");

% plotting
theta2 = linspace(0.001, pi/5);
theta1 = linspace(0.001, pi/5);

[x,y] = meshgrid(theta1,theta2);

%z = charge1(x,y);
%surf(x,y,z);
plot(theta2, charge1(pi/3,theta2));

% defining functions
function q1 = charge1(t1,t2)
    % electromagnetic constant
    epsilon0 = 8.85 * 10^-12;
    % graviational constant
    g = 9.81;

    % length of the ropes
    l = 1;
    % weight of one sphere
    m = 0.1;
    q1 = sqrt(16 * pi * epsilon0 * 4 * l^2 * (sin(t2/2)).^2 .* tan(t2/2) *m*g)./2 + 4*l*sqrt(m*g*pi*epsilon0)*sqrt((sin(t2/2)).^2 .* tan(t2/2) - (sin(t1/2)).^2 .* tan(t1/2));
    if t2 < t1
        q1 = -1;
    end
end

function q2 = charge2(t1,t2)
    % electromagnetic constant
    epsilon0 = 8.85 * 10^-12;
    % graviational constant
    g = 9.81;
    % length of the ropes
    l = 1;
    % weight of one sphere
    m = 0.1;
    q2 = sqrt(16 * pi * epsilon0 * 4 * l^2 * (sin(t2/2))^2 * tan(t2/2) *m*g)/2 - 4*l*sqrt(m*g*pi*epsilon0)*sqrt((sin(t2/2))^2 * tan(t2/2) - (sin(t1/2))^2 * tan(t1/2));
end