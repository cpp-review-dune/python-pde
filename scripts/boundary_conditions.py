#!/usr/bin/env python

from pde import DiffusionPDE, ScalarField, UnitGrid

grid = UnitGrid(shape=[32, 32], periodic=[False, True])
state = ScalarField.random_uniform(grid=grid, vmin=0.2, vmax=0.3)

bc_x_left = {"derivative": 0.1}
bc_x_right = {"value": "sin(y / 2)"}
bc_x = [bc_x_left, bc_x_right]
bc_y = "periodic"
eq = DiffusionPDE(bc=[bc_x, bc_y])

result = eq.solve(state=state, t_range=10, dt=0.005)
result.plot()
