#!/usr/bin/env python

from pde import CartesianGrid, ScalarField, solve_poisson_equation

grid = CartesianGrid(bounds=[[0, 1]], shape=32, periodic=False)
field = ScalarField(grid=grid, data=1)
result = solve_poisson_equation(rhs=field, bc=[{"value": 0}, {"derivative": 1}])

result.plot()
