#!/usr/bin/env python

from pde import FieldCollection, PDEBase, PlotTracker, ScalarField, UnitGrid


class SIRPDE(PDEBase):
    """SIR-model with diffusive mobility"""

    def __init__(
        self, beta=0.3, gamma=0.9, diffusivity=0.1, bc="auto_periodic_neumann"
    ):
        super().__init__()
        self.beta = beta
        self.gamma = gamma
        self.diffusivity = diffusivity
        self.bc = bc

    def get_state(self, s, i):
        """generate a suitable initial state"""
        norm = (s + i).data.max()
        if norm > 1:
            s /= norm
            i /= norm
        s.label = "Susceptible"
        i.label = "Infected"

        r = ScalarField(grid=s.grid, data=1 - s - i, label="Recovered")
        return FieldCollection(fields=[s, i, r])

    def evolution_rate(self, state, t=0):
        s, i, r = state
        diff = self.diffusivity
        ds_dt = diff * s.laplace(self.bc) - self.beta * i * s
        di_dt = diff * i.laplace(self.bc) + self.beta * i * s - self.gamma * i
        dr_dt = diff * r.laplace(self.bc) + self.gamma * i
        return FieldCollection(fields=[ds_dt, di_dt, dr_dt])


eq = SIRPDE(beta=2, gamma=0.1)

grid = UnitGrid(shape=[32, 32])
s = ScalarField(grid=grid, data=1)
i = ScalarField(grid=grid, data=0)
i.data[0, 0] = 1
state = eq.get_state(s=s, i=i)

tracker = PlotTracker(interval=10, plot_args={"vmin": 0, "vmax": 1})
sol = eq.solve(state=state, t_range=50, dt=1e-2, tracker=["progress", tracker])
