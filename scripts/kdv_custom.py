#!/usr/bin/env python

from math import pi
from pde import CartesianGrid, MemoryStorage, PDEBase, ScalarField, plot_kymograph


class KortewegDeVriesPDE(PDEBase):
    """Korteweg-de Vries equation"""

    def evolution_rate(self, state, t=0):
        """implement the python version of the evolution equation"""
        assert state.grid.dim == 1  # ensure the state is one-dimensional
        grad_x = state.gradient("auto_periodic_neumann")[0]
        return 6 * state * grad_x - grad_x.laplace("auto_periodic_neumann")


grid = CartesianGrid(bounds=[[0, 2 * pi]], shape=[32], periodic=True)
state = ScalarField.from_expression(grid=grid, expression="sin(x)")

storage = MemoryStorage()
eq = KortewegDeVriesPDE()
eq.solve(state=state, t_range=3, method="scipy", tracker=storage.tracker(0.1))

plot_kymograph(storage=storage)
