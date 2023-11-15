#!/usr/bin/env python

from math import pi

from pde import CartesianGrid, solve_laplace_equation

grid = CartesianGrid(bounds=[[0, 2 * pi]] * 2, shape=64)
bcs = [{"value": "sin(y)"}, {"value": "sin(x)"}]

res = solve_laplace_equation(grid=grid, bc=bcs)
res.plot()
