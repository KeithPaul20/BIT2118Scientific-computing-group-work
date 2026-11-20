import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Delivery Fleet Cost Optimization

# x = Number of Small Trucks
# y = Number of Large Trucks

# Cost Function
def operating_cost(z):
    x, y = z
    return 8000 * x + 12000 * y

# Delivery Capacity Constraint
def capacity_constraint(z):
    x, y = z
    return 500 * x + 900 * y - 5000

constraints = {
    "type": "ineq",
    "fun": capacity_constraint
}

bounds = [
    (0, None),
    (0, None)
]

solution = minimize(
    operating_cost,
    x0=[5, 3],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x

print("Optimization Success:", solution.success)
print(f"Small Trucks: {x:.2f}")
print(f"Large Trucks: {y:.2f}")

print(
    f"Total Delivery Capacity: "
    f"{500*x + 900*y:.2f} kg"
)

print(
    f"Minimum Operating Cost: "
    f"KES {solution.fun:.2f}"
)

# Integer solution search
best_integer = None

for small in range(20):
    for large in range(20):

        capacity = 500 * small + 900 * large

        if capacity >= 5000:

            cost = (
                8000 * small +
                12000 * large
            )

            if (
                best_integer is None or
                cost < best_integer[0]
            ):
                best_integer = (
                    cost,
                    small,
                    large,
                    capacity
                )

print("\nBest Integer Solution:")
print(best_integer)

# Visualization
small_range = np.linspace(0, 15, 100)

required_large = (
    5000 - 500 * small_range
) / 900

plt.plot(
    small_range,
    required_large,
    label="Capacity Constraint"
)

plt.xlabel("Small Trucks")
plt.ylabel("Large Trucks")
plt.title("Fleet Optimization Constraint")

plt.grid(True)
plt.legend()

plt.show()