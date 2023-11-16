#!/usr/bin/env python

from pde import CylindricalSymGrid, ScalarField, DiffusionPDE

grid = CylindricalSymGrid(radius=5, bounds_z=[0, 1], shape=(32, 8))
field = ScalarField.from_expression(grid=grid, expression="sqrt(z) * exp(-r**2)")
field.plot()


eq = DiffusionPDE()
result = eq.solve(state=field, t_range=[0, 10])
result.plot()
