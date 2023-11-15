#!/usr/bin/env python

from math import pi

from pde import PDE, CartesianGrid, MemoryStorage, ScalarField, plot_kymograph

eq = PDE(rhs={"φ": "6 * φ * d_dx(φ) - laplace(d_dx(φ))"})
grid = CartesianGrid(bounds=[[0, 2 * pi]], shape=[32], periodic=True)
state = ScalarField.from_expression(grid=grid, expression="sin(x)")

storage = MemoryStorage()
eq.solve(state=state, t_range=3, method="scipy", tracker=storage.tracker(0.1))

plot_kymograph(storage)
