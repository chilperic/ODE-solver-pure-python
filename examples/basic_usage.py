'''Basic usage examples'''
from pyodesolve import solve_ivp

print("PyODESolve - Basic Examples")
print("=" * 60)

# Example 1: Exponential decay
print("\n1. Exponential Decay")
print("-" * 60)

def exponential_decay(t, y):
    return [-0.5 * y[0]]

result = solve_ivp(exponential_decay, (0, 10), [1.0])
print(f"Final value: {result.y[-1][0]:.6f}")
print(f"Steps: {result.stats.n_steps}")
print(f"Function evals: {result.stats.n_function_evals}")

# Example 2: Lorenz attractor
print("\n2. Lorenz Attractor")
print("-" * 60)

def lorenz(t, y):
    sigma, rho, beta = 10, 28, 8/3
    return [
        sigma * (y[1] - y[0]),
        y[0] * (rho - y[2]) - y[1],
        y[0] * y[1] - beta * y[2]
    ]

result = solve_ivp(lorenz, (0, 50), [1, 1, 1], method='DOP853')
print(f"Success: {result.success}")
print(f"Steps: {result.stats.n_steps}")
print(f"Final state: [{result.y[-1][0]:.3f}, {result.y[-1][1]:.3f}, {result.y[-1][2]:.3f}]")

print("\n" + "=" * 60)
print("✓ Examples completed successfully!")
