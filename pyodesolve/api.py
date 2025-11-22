'''High-level API'''
from typing import Callable, Tuple, List, Optional, Any
from .core.result import ODEResult
from .explicit.dormand_prince import DormandPrince
from .implicit.bdf import BDF
from .implicit.radau import RadauIIA

def solve_ivp(
    fun: Callable,
    t_span: Tuple[float, float],
    y0: List[float],
    method: str = 'DOP853',
    rtol: float = 1e-3,
    atol: float = 1e-6,
    jac: Optional[Callable] = None,
    jac_sparsity: Optional[Any] = None,
    vectorized: bool = False,
    first_step: Optional[float] = None,
    max_step: float = float('inf'),
    **options
) -> ODEResult:
    '''
    Solve ODE system.

    See full docstring in artifact.
    '''

    methods = {
        'DOP853': DormandPrince,
        'RK45': DormandPrince,
        'BDF': BDF,
        'Radau': RadauIIA,
    }

    if method not in methods:
        raise ValueError(f"Unknown method: {method}")

    solver_class = methods[method]
    solver = solver_class(
        fun=fun, t_span=t_span, y0=y0, rtol=rtol, atol=atol,
        jac=jac, jac_sparsity=jac_sparsity, vectorized=vectorized,
        first_step=first_step, max_step=max_step, **options
    )

    return solver.solve()
