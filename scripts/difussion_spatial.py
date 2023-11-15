#!/usr/bin/env python

from pde import PDE, CartesianGrid, MemoryStorage, ScalarField, plot_kymograph

diffusivity = "1.01 + tanh(x)"
term_1 = f"({diffusivity}) * laplace(c)"
term_2 = f"dot(gradient({diffusivity}), gradient(c))"
eq = PDE(rhs={"c": f"{term_1} + {term_2}"}, bc={"value": 0})


grid = CartesianGrid(bounds=[[-5, 5]], shape=64)
field = ScalarField(grid=grid, data=1)

storage = MemoryStorage()
res = eq.solve(state=field, t_range=100, dt=1e-3, tracker=storage.tracker(1))

plot_kymograph(storage)
