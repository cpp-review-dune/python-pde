#!/usr/bin/env python

from pde import DiffusionPDE, ScalarField, UnitGrid

grid = UnitGrid(shape=[64, 64])
state = ScalarField.random_uniform(grid=grid, vmin=0.2, vmax=0.3)

eq = DiffusionPDE(diffusivity=0.1)
result = eq.solve(state=state, t_range=10)
result.plot()
