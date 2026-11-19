import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# Water tank equilibrium model
# Inflow rate = Outflow rate at equilibrium

def water_balance(h):
    return h - 10 - 5 * np.exp(-h / 8)

# Bisection Method
solution = root_scalar(
    water_balance,
    bracket=[10, 20],
    method="bisect",
    xtol=1e-10
)

# Fixed-Point Iteration
# h = 10 + 5*exp(-h/8)

def g(h):
    return 10 + 5 * np.exp(-h / 8)

h = 15.0
history = [h]

for _ in range(100):
    h_new = g(h)
    history.append(h_new)

    if abs(h_new - h) < 1e-10:
        break

    h = h_new

print(f"Equilibrium Water Level (Bisection): {solution.root:.6f} m")
print(f"Equilibrium Water Level (Fixed-Point): {history[-1]:.6f} m")
print("Iterations:", len(history) - 1)

# Graph
levels = np.linspace(10, 20, 300)

plt.plot(levels, water_balance(levels))
plt.axhline(0, color='black')
plt.axvline(solution.root, linestyle='--', color='red')

plt.xlabel("Water Level (m)")
plt.ylabel("Water Balance Function")
plt.title("Reservoir Equilibrium Water Level")
plt.grid(True)

plt.show()