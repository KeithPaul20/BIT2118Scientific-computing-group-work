import numpy as np
import matplotlib.pyplot as plt

# Hospital Emergency Room Simulation

rng = np.random.default_rng(42)

# Hospital can handle 50 patients per day
capacity = 50

# Average daily patients = 42
mean_patients = 42

# Standard deviation = 8
std_patients = 8

# Number of simulations
N = 100000

# Generate random patient arrivals
daily_patients = rng.normal(
    mean_patients,
    std_patients,
    N
)

# Days when ER exceeds capacity
overloaded = daily_patients > capacity

overload_probability = overloaded.mean()

print(
    f"Estimated Overload Probability: "
    f"{overload_probability:.4%}"
)

print(
    f"Overloaded Days: "
    f"{overloaded.sum()} out of {N}"
)

# Running estimate
running_probability = (
    np.cumsum(overloaded)
    / np.arange(1, N + 1)
)

indices = np.unique(
    np.logspace(
        1,
        np.log10(N),
        200
    ).astype(int)
) - 1

plt.semilogx(
    indices + 1,
    running_probability[indices]
)

plt.xlabel("Number of Simulations")
plt.ylabel("Estimated Overload Probability")

plt.title(
    "Monte Carlo Simulation of ER Overload Risk"
)

plt.grid(True)

plt.show()