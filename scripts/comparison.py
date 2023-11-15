#!/usr/bin/env python

from pde import (
    UnitGrid,
    ScalarField,
    DiffusionPDE,
    ExplicitSolver,
    Controller,
    ScipySolver,
    FieldCollection,
)

grid = UnitGrid(shape=[32, 32])
field = ScalarField.random_uniform(grid=grid, vmin=-1, vmax=1)
eq = DiffusionPDE()

solver1 = ExplicitSolver(pde=eq)
controller1 = Controller(solver=solver1, t_range=1, tracker=None)
sol1 = controller1.run(initial_state=field, dt=1e-3)
sol1.label = "explicit solver"
print("Diagnostic information from first run:")
print(controller1.diagnostics)
print()

solver2 = ExplicitSolver(pde=eq, scheme="runge-kutta", adaptive=True)
controller2 = Controller(solver=solver2, t_range=1, tracker=None)
sol2 = controller2.run(initial_state=field, dt=1e-3)
sol2.label = "explicit, adaptive solver"
print("Diagnostic information from second run:")
print(controller2.diagnostics)
print()


solver3 = ScipySolver(pde=eq)
controller3 = Controller(solver=solver3, t_range=1, tracker=None)
sol3 = controller3.run(initial_state=field)
sol3.label = "scipy solver"
print("Diagnostic information from third run:")
print(controller3.diagnostics)
print()

title = f"Deviation: {((sol1 - sol2)**2).average:.2g}, {((sol1 - sol3)**2).average:.2g}"
FieldCollection(fields=[sol1, sol2, sol3]).plot(title=title)
