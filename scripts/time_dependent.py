#!/usr/bin/env python

from pde import PDE, CartesianGrid, MemoryStorage, ScalarField, plot_kymograph

grid = CartesianGrid(bounds=[[0, 10]], shape=[64])
state = ScalarField(grid=grid)

eq = PDE(rhs={"c": "laplace(c)"}, bc={"value_expression": "sin(t)"})

storage = MemoryStorage()
eq.solve(state=state, t_range=20, dt=1e-4, tracker=storage.tracker(0.1))

plot_kymograph(storage)
