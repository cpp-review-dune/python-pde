#!/usr/bin/env -S octave -qf

% fds_example.m by John Shiach
%
% This program solves the linear advection equation using a first order FDS

% Clear workspaces (should always be done at the start of an m-file)

clc
clearvars

% Define variables
N = 11; % number of nodes
xmin = 0; % min value of x
xmax = 1; % max value of x
dt = 0.05; % time step
v = 1; % velocity
t = 0; % initial value of t

% Calculate node positions
dx = (xmax - xmin) / (N - 1);
x = xmin:dx:xmax;

% Calculate initial conditions
u = exp(-100 * (x - 0.4).^2);

% Output column headings and initial conditions to the command window
hline = repmat('-', 1, 9 * (N + 1));
fprintf('\n%s', hline)
fprintf('\n    t   ')
fprintf('|   u_%1i  ', [0:N - 1])
fprintf('\n%s', hline)
fprintf('\n %6.2f ', t)
fprintf('|%7.4f ', u)

% pre-calculate C = v * dt / dx
C = v * dt / dx;

% Perform 3 iterations of the FDS
for n = 1:3

    % Calculate boundary conditions
    u(1) = 0;
    u(N) = 0;

    % Calculate new values of u
    unew = u;

    for i = 2:N - 1
        unew(i) = u(i) - C * (u(i) - u(i - 1));
    end

    % Update t and u
    t = t + dt;
    u = unew;

    % Output current solution
    fprintf('\n %6.2f ', t)
    fprintf('|%7.4f ', u)
end

fprintf('\n%s\n\n', hline)
