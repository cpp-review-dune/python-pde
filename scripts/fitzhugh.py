#!/usr/bin/env python

from pde import FieldCollection, PDEBase, UnitGrid


class FitzhughNagumoPDE(PDEBase):
    """FitzHugh-Nagumo model with diffusive coupling"""

    def __init__(self, stimulus=0.5, τ=10, a=0, b=0, bc="auto_periodic_neumann"):
        super().__init__()
        self.bc = bc
        self.stimulus = stimulus
        self.τ = τ
        self.a = a
        self.b = b

    def evolution_rate(self, state, t=0):
        v, w = state

        v_t = v.laplace(bc=self.bc) + v - v**3 / 3 - w + self.stimulus
        w_t = (v + self.a - self.b * w) / self.τ

        return FieldCollection([v_t, w_t])


grid = UnitGrid(shape=[32, 32])
state = FieldCollection.scalar_random_uniform(num_fields=2, grid=grid)

eq = FitzhughNagumoPDE()
result = eq.solve(state=state, t_range=100, dt=0.01)
result.plot()
