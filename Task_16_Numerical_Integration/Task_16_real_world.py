import numpy as np
from scipy.integrate import simpson
import matplotlib.pyplot as plt

# River Flow Monitoring

time_hours = np.array(
    [0, 2, 4, 6, 8, 10, 12],
    dtype=float
)

flow_rate = np.array(
    [45, 52, 67, 75, 70, 60, 50],
    dtype=float
)

# Numerical Integration
total_volume_trapezoid = np.trapezoid(
    flow_rate,
    time_hours
)

total_volume_simpson = simpson(
    flow_rate,
    x=time_hours
)

print(
    f"Total Water Volume (Trapezoidal Rule): "
    f"{total_volume_trapezoid:.2f} m³"
)

print(
    f"Total Water Volume (Simpson's Rule): "
    f"{total_volume_simpson:.2f} m³"
)

print(
    f"Difference: "
    f"{abs(total_volume_simpson - total_volume_trapezoid):.2f} m³"
)

# Plot of flow rate
plt.plot(
    time_hours,
    flow_rate,
    marker='o'
)

plt.xlabel("Time (Hours)")
plt.ylabel("Flow Rate (m³/h)")
plt.title("River Flow Rate Measurements")

plt.grid(True)
plt.show()