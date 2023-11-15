#!/usr/bin/env python

import numpy as np

from pde import CartesianGrid, DiffusionPDE, ScalarField

grid = CartesianGrid(bounds=[[-5, 5], [-5, 5]], shape=32)
field = ScalarField(grid=grid)


def bc_value(adjacent_value, dx, x, y, t):
    """return boundary value"""
    return np.sign(x)


bc_x = "derivative"
bc_y = ["derivative", {"value_expression": bc_value}]

eq = DiffusionPDE(bc=[bc_x, bc_y])
res = eq.solve(state=field, t_range=10, dt=0.01, backend="numpy")
res.plot()
