#!/usr/bin/env python

from pde import CartesianGrid, VectorField

grid = CartesianGrid(bounds=[[-2, 2], [-2, 2]], shape=32)
field = VectorField.from_expression(grid=grid, expressions=["sin(x)", "cos(x)"])
field.plot(method="streamplot", title="Stream plot")
