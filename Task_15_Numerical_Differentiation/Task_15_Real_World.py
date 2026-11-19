import numpy as np
import matplotlib.pyplot as plt

# Fuel Consumption Analysis

time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)

fuel_used = np.array([
    0.0, 2.5, 5.8, 9.6, 14.0, 19.0, 25.0
])

consumption_rate = np.zeros_like(fuel_used)

# Forward difference
consumption_rate[0] = (
    fuel_used[1] - fuel_used[0]
) / (
    time[1] - time[0]
)

# Central difference
for i in range(1, len(time) - 1):
    consumption_rate[i] = (
        fuel_used[i + 1] - fuel_used[i - 1]
    ) / (
        time[i + 1] - time[i - 1]
    )

# Backward difference
consumption_rate[-1] = (
    fuel_used[-1] - fuel_used[-2]
) / (
    time[-1] - time[-2]
)

for t, fuel, rate in zip(
    time,
    fuel_used,
    consumption_rate
):
    print(
        f"Time = {t:.0f} h, "
        f"Fuel Used = {fuel:.1f} L, "
        f"Consumption Rate = {rate:.2f} L/h"
    )

plt.plot(
    time,
    consumption_rate,
    marker="o"
)

plt.xlabel("Time (Hours)")
plt.ylabel("Fuel Consumption Rate (L/h)")
plt.title("Vehicle Fuel Consumption Rate")

plt.grid(True)
plt.show()