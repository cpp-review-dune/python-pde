#!/usr/bin/env python

import numba as nb
from pde import PDEBase, ScalarField, UnitGrid


class KuramotoSivashinskyPDE(PDEBase):
    """Implementation of the normalized Kuramoto-Sivashinsky equation"""

    def __init__(self, bc="auto_periodic_neumann"):
        super().__init__()
        self.bc = bc

    def evolution_rate(self, state, t=0):
        """implement the python version of the evolution equation"""
        state_lap = state.laplace(bc=self.bc)
        state_lap2 = state_lap.laplace(bc=self.bc)
        state_grad_sq = state.gradient_squared(bc=self.bc)
        return -state_grad_sq / 2 - state_lap - state_lap2

    def _make_pde_rhs_numba(self, state):
        """nunmba-compiled implementation of the PDE"""
        gradient_squared = state.grid.make_operator("gradient_squared", bc=self.bc)
        laplace = state.grid.make_operator("laplace", bc=self.bc)

        @nb.jit
        def pde_rhs(data, t):
            return -0.5 * gradient_squared(data) - laplace(data + laplace(data))

        return pde_rhs


grid = UnitGrid(shape=[32, 32])  # generate grid
state = ScalarField.random_uniform(grid=grid)  # generate initial condition

eq = KuramotoSivashinskyPDE()  # define the pde
result = eq.solve(state=state, t_range=10, dt=0.01)
result.plot()
