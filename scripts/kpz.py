#!/usr/bin/env python

from pde import KPZInterfacePDE, MemoryStorage, ScalarField, UnitGrid, plot_kymograph

grid = UnitGrid(shape=[64])
state = ScalarField.random_harmonic(grid=grid)

eq = KPZInterfacePDE(noise=1)
storage = MemoryStorage()
eq.solve(state=state, t_range=10, dt=0.01, tracker=storage.tracker(0.5))
plot_kymograph(storage)
