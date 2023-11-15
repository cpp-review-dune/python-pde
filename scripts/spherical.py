#!/usr/bin/env python

from pde import DiffusionPDE, ScalarField, SphericalSymGrid

grid = SphericalSymGrid(radius=[1, 5], shape=128)
state = ScalarField.random_uniform(grid=grid)

eq = DiffusionPDE(diffusivity=0.1)
result = eq.solve(state=state, t_range=0.1, dt=0.001)

result.plot(kind="image")
