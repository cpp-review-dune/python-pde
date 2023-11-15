#!/usr/bin/env python

from math import sqrt
from pde import PDE, CartesianGrid, MemoryStorage, ScalarField, plot_kymograph

grid = CartesianGrid(bounds=[[0, 20]], shape=128, periodic=False)

initial_state = ScalarField.from_expression(
    grid=grid, expression="exp(I * 5 * x) * exp(-(x - 10)**2)"
)
initial_state /= sqrt(initial_state.to_scalar(scalar="norm_squared").integral.real)

eq = PDE(rhs={"ψ": f"I * laplace(ψ)"})


storage = MemoryStorage()
eq.solve(state=initial_state, t_range=2.5, dt=1e-5, tracker=[storage.tracker(0.02)])

plot_kymograph(storage=storage, scalar="norm_squared")
