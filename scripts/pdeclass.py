#!/usr/bin/env python

from pde import PDE, ScalarField, UnitGrid

grid = UnitGrid(shape=[32, 32])
state = ScalarField.random_uniform(grid=grid)

eq = PDE(rhs={"u": "-gradient_squared(u) / 2 - laplace(u + laplace(u))"})
result = eq.solve(state=state, t_range=10, dt=0.01)
result.plot()
