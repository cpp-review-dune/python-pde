#!/usr/bin/env python

from pde import (
    UnitGrid,
    ScalarField,
    MemoryStorage,
    PlotTracker,
    PrintTracker,
    RealtimeInterrupts,
    DiffusionPDE,
)

grid = UnitGrid(shape=[32, 32])
state = ScalarField.random_uniform(grid=grid)

storage = MemoryStorage()

trackers = [
    "progress",
    "steady_state",
    storage.tracker(interval=1),
    PlotTracker(show=True),
    PrintTracker(interval=RealtimeInterrupts(duration=5)),
]

eq = DiffusionPDE(0.1)
eq.solve(state=state, t_range=3, dt=0.1, tracker=trackers)

for field in storage:
    print(field.integral)
