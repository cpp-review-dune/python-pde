#!/usr/bin/env python

import matplotlib.pyplot as plt
from math import pi

from pde import CylindricalSymGrid, ScalarField

grid = CylindricalSymGrid(radius=7, bounds_z=[0, 4 * pi], shape=64)
data = ScalarField.from_expression(grid=grid, expression="sin(z) * exp(-r / 3)")
data += 0.05 * ScalarField.random_normal(grid=grid)

smoothed = data.smooth()
projected = data.project(axes="r")
sliced = smoothed.slice(position={"z": 1})

fig, axes = plt.subplots(nrows=2, ncols=2)
data.plot(ax=axes[0, 0], title="Original field")
smoothed.plot(ax=axes[1, 0], title="Smoothed field")
projected.plot(ax=axes[0, 1], title="Projection on axial coordinate")
sliced.plot(ax=axes[1, 1], title="Slice of smoothed field at $z=1$")
plt.subplots_adjust(hspace=0.8)
plt.show()
