#!/usr/bin/env -S octave -qf

% oned_swe.m by John Shiach
%
% This program solves the SWE using the Lax-Friedrichs scheme

% Clear workspaces

clc
clearvars
close all

function dt = calculate_dt(U, dx, t, tmax)

    % This function calculates the maximum allowable time step
    global gravity
    dt = 0.9 * dx / max(abs(U(2, :) ./ U(1, :)) + sqrt(gravity * U(1, :)));
    dt = min(dt, tmax - t);

end

function U = calculate_BC(U)

    % This function calculates the values of the ghost nodes using transmissive
    % boundary conditions

    U(:, 1) = U(:, 3);
    U(:, end) = U(:, end - 2);

end

function F = calculate_F(U)

    % This function calculates the flux vector F from U.
    global gravity
    F(1, :) = U(2, :);
    F(2, :) = U(2, :).^2 ./ U(1, :) + 0.5 * gravity * U(1, :).^2;
end

function Unp1 = Lax_Friedrichs(U, F, dt, dx)

    % This function calculates a single step of the Lax-Friedrichs scheme

    N = size(U, 2) - 2;
    Unp1 = U;
    C = 0.5 * dt / dx;

    for i = 2:N + 1
        Unp1(:, i) = 0.5 * (U(:, i + 1) + U(:, i - 1)) - C * (F(:, i +1) - F(:, i - 1));
    end

end

% Define global parameters
global gravity
gravity = 9.81; % acceleration due to gravity

% Define variables
N = 101; % number of nodes
xmin = 0; % lower bound of x
xmax = 1; % upper bound of x
hL = 1; % water height to the left of the dam
hR = 0.5; % water height to the right of the dam
t = 0; % time variable
tmax = 0.1; % max value of t

% Define spatial array (including ghost nodes)
dx = (xmax - xmin) / (N - 1);
x = xmin - dx:dx:xmax + dx;

% Define initial conditions
U = zeros(2, length(x));
U(1, x <= 0.5) = hL;
U(1, x > 0.5) = hR;

% Time marching loop
while t < tmax

    % Calculate maximum allowable time step
    dt = calculate_dt(U, dx, t, tmax);

    % Calculate boundary conditions
    U = calculate_BC(U);

    % Calculate F vector
    F = calculate_F(U);

    % Calculate one step of the Lax-Friedrichs scheme
    U = Lax_Friedrichs(U, F, dt, dx);

    % Update t
    t = t + dt;

    % Plot current solution
    num_plot = plot(x, U(1, :), 'o-', 'markerfacecolor', 'blue');
    axis([xmin, xmax, 0, 1.2])
    xlabel('$x$', 'fontsize', 16, 'interpreter', 'latex')
    ylabel('$h$', 'fontsize', 16, 'interpreter', 'latex')
    title(sprintf('$t = %1.3f$', t), 'fontsize', 16, 'interpreter', 'latex')
    shg
    pause(0.001)
end

% Plot numerical solution against exact solution
% load dambreak_exact
% hold on
% exact_plot = plot(xexact, hexact, 'r-', 'linewidth', 2);
% hold off
% leg = legend([exact_plot, num_plot], 'exact solution', 'numerical solution');
% set(leg, 'fontsize', 14, 'interpreter', 'latex')
