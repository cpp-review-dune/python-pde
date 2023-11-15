#!/usr/bin/env python

from pde import CartesianGrid, DiffusionPDE, ScalarField

grid = CartesianGrid(bounds=[[-1, 1], [0, 2]], shape=[30, 16])
state = ScalarField(grid=grid)
state.insert(point=[0, 1], amount=1)

eq = DiffusionPDE(diffusivity=0.1)
result = eq.solve(state=state, t_range=1, dt=0.01)
result.plot(cmap="magma")
