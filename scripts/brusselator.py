#!/usr/bin/env python

from pde import PDE, FieldCollection, PlotTracker, ScalarField, UnitGrid

a, b = 1, 3
d0, d1 = 1, 0.1
eq = PDE(
    rhs={
        "u": f"{d0} * laplace(u) + {a} - ({b} + 1) * u + u**2 * v",
        "v": f"{d1} * laplace(v) + {b} * u - u**2 * v",
    }
)

grid = UnitGrid(shape=[64, 64])
u = ScalarField(grid=grid, data=a, label="Field $u$")
v = b / a + 0.1 * ScalarField.random_normal(grid=grid, label="Field $v$")
state = FieldCollection(fields=[u, v])

tracker = PlotTracker(interval=1, plot_args={"vmin": 0, "vmax": 5})
sol = eq.solve(state=state, t_range=20, dt=1e-3, tracker=tracker)
