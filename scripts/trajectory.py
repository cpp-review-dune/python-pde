#!/usr/bin/env python


from tempfile import NamedTemporaryFile

from pde import (
    UnitGrid,
    FieldCollection,
    ScalarField,
    VectorField,
    PDE,
    FileStorage,
    plot_kymographs,
)

grid = UnitGrid(shape=[32])
state = FieldCollection(
    [ScalarField.random_uniform(grid=grid), VectorField.random_uniform(grid=grid)]
)
eq = PDE(rhs={"s": "-0.1 * s", "v": "-v"})

# get a temporary file to write data to
path = NamedTemporaryFile(suffix=".hdf5")

# run a simulation and write the results
writer = FileStorage(filename=path.name, write_mode="truncate")
eq.solve(state=state, t_range=32, dt=0.01, tracker=writer.tracker(1))

# read the simulation back in again
reader = FileStorage(filename=path.name, write_mode="read_only")
plot_kymographs(reader)
