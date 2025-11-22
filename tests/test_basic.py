'''Basic tests'''
from pyodesolve import solve_ivp

def test_exponential_decay():
    def f(t, y):
        return [-0.5 * y[0]]

    result = solve_ivp(f, (0, 10), [1.0], method='DOP853')
    assert result.success
    assert abs(result.y[-1][0] - 0.00674) < 0.001

def test_harmonic_oscillator():
    def f(t, y):
        return [y[1], -y[0]]

    result = solve_ivp(f, (0, 20), [1.0, 0.0], method='DOP853', rtol=1e-8)

    # Energy conservation
    E0 = 0.5
    Ef = 0.5 * (result.y[-1][0]**2 + result.y[-1][1]**2)
    assert abs(Ef - E0) / E0 < 1e-6
