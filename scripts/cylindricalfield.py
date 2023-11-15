#!/usr/bin/env python

from pde import CylindricalSymGrid, ScalarField

grid = CylindricalSymGrid(radius=3, bounds_z=[0, 4], shape=16)
field = ScalarField.from_expression(grid=grid, expression="sqrt(z) * exp(-r**2)")
field.plot(title="Scalar field in cylindrical coordinates")
