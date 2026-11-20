import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Drug Concentration in Bloodstream

initial_concentration = 100.0  # mg/L
elimination_rate = 0.25        # per hour

def drug_decay(t, C):
    return [-elimination_rate * C[0]]

time_points = np.linspace(0, 12, 200)

solution = solve_ivp(
    drug_decay,
    (0, 12),
    [initial_concentration],
    t_eval=time_points,
    rtol=1e-9,
    atol=1e-11
)

# Exact solution
exact_solution = (
    initial_concentration *
    np.exp(-elimination_rate * solution.t)
)

print("Solver Success:", solution.success)

print(
    f"Drug Concentration After 12 Hours: "
    f"{solution.y[0, -1]:.2f} mg/L"
)

print(
    f"Maximum Error: "
    f"{np.max(np.abs(solution.y[0] - exact_solution)):.6e}"
)

plt.plot(
    solution.t,
    solution.y[0],
    label="solve_ivp Solution"
)

plt.plot(
    solution.t,
    exact_solution,
    linestyle="--",
    label="Exact Solution"
)

plt.xlabel("Time (Hours)")
plt.ylabel("Drug Concentration (mg/L)")
plt.title("Drug Elimination from the Bloodstream")

plt.legend()
plt.grid(True)

plt.show()