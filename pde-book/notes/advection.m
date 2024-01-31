#!/usr/bin/env -S octave -qf

% advection.m by John Shiach
%
% This program solves the advection equation using the FOU scheme

% Clear workspaces
clc
clearvars
close all

% Define variables
N = 101; % number of nodes
xmin = 0; % lower bound of x
xmax = 1; % upper bound of x
v = 0.5; % velocity
t = 0; % time variable
tmax = 1; % max value of t
dt = 0.01; % time step

% Discretise the domain (remember to include ghost nodes)
dx = (xmax - xmin) / (N - 1);
x = xmin - dx:dx:xmax + dx;

function u = f(x)

    % This function defines the initial profile.
    u = exp(-200 * (x - 0.25).^2);
end

% Define initial conditions
u = f(x); % solution array u^n

% Time marching loop
while t < tmax

    % Ensure that t does not exceed tmax
    dt = min(dt, tmax - t);

    % Calculate boundary conditions
    u(1) = u(3);
    u(N + 2) = u(N);

    % Calculate values of u^(n + 1) using the FOU scheme
    unew = u;
    C = v * dt / dx;

    for i = 2:N + 1
        unew(i) = u(i) - C * (u(i) - u(i -1));
    end

    % Update u and t
    u = unew;
    t = t + dt;

    % Calculate exact solution
    uexact = f(x - v * t);

    % Plot the numerical against the exact solution
    plot(x, uexact, 'r-', 'linewidth', 2)
    hold on
    plot(x, u, 'bo-', 'markerfacecolor', 'b')
    hold off
    axis([xmin, xmax, -0.5, 1.5])
    xlabel('$x$', 'fontsize', 16, 'interpreter', 'latex')
    ylabel('$u(t, x)$', 'fontsize', 16, 'interpreter', 'latex')
    title(sprintf('$t = %1.3f$ s', t), 'fontsize', 16, 'interpreter', 'latex')
    shg
    pause(0.001)
end

% Add legends to plot
leg = legend('exact solution', 'numerical solution');
set(leg, 'fontsize', 12, 'interpreter', 'latex')
