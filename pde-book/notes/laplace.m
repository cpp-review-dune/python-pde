#!/usr/bin/env -S octave -qf

% laplace.m by John Shiach
%
% This program calculates the solution to the Laplace equation using the
% Jacobi method

clc
clearvars
close all

% define variables
Nx = 5; % no. of nodes in the x direction (inc ghost nodes)
Ny = 4; % no. of nodes in the y direction (inc ghost nodes)
lenx = 4; % length of the x domain
leny = 3; % length of the y domain
err = 1; % error between sucessive iterations
tol = 1e-6; % convergence tolerance
k = 0; % iteration counter

% Calculate x and y node co-ordinates
dx = lenx / (Nx - 1);
dy = leny / (Ny - 1);
x = 0:dx:lenx;
y = 0:dy:leny;
[x, y] = meshgrid(x, y);

% Initialise solution array
u = [8.9 8.9 8.9 8.9 8.9;
    8.4 0.0 0.0 0.0 9.2;
    7.2 0.0 0.0 0.0 9.4;
    6.1 6.8 7.7 8.7 9.8];

u = flipud(u); % invert u to be consistent with matrix indexing

% output column heading and initial values
hline = repmat('-', 1, 12 * ((Nx - 2) * (Ny - 2) + 2));
fprintf('%s\n     k    |', hline)

for j = 1:Ny - 2

    for i = 1:Nx - 2
        fprintf('   u(%1i, %1i) |', i, j)
    end

end

fprintf('  L2 error\n%s \n   %4i   ', hline, k)
fprintf('|%10.6f ', u(2:Ny - 1, 2:Nx - 1)')
fprintf('|%10.6f\n', err)

% perform iterations until convergence
while err > tol

    % calculate improved estimate using the Jacobi method
    unew = u;

    for j = 2:Ny - 1

        for i = 2:Nx - 1
            unew(j, i) = (u(j + 1, i) + u(j, i + 1) + u(j - 1, i) + u(j, i - 1)) / 4;
        end

    end

    % calculate absolute error
    err = sqrt(sum(sum((unew - u).^2)));

    % update u
    u = unew;
    k = k + 1;

    % output current solution
    fprintf('   %4i   ', k)
    fprintf('|%10.6f ', u(2:Ny-1, 2:Nx-1)')
    fprintf('|%10.6f \n', err)

end

fprintf('%s\n', hline)

% Plot solution
surf(x, y, u)
xlabel('$x$', 'fontsize', 16, 'interpreter', 'latex')
ylabel('$y$', 'fontsize', 16, 'interpreter', 'latex')
zlabel('$U(x, y)$', 'fontsize', 16, 'interpreter', 'latex')
