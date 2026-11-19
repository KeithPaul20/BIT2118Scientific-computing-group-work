import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

# Water tank monitoring system
# Measurements collected every 2 hours

hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)

water_level = np.array([
    3.5, 4.1, 5.2, 6.0, 5.8, 5.0, 4.2
])

# Interpolation functions
linear = interp1d(hours, water_level, kind="linear")
cubic = CubicSpline(hours, water_level)

# Estimate values every 30 minutes
times = np.arange(0, 12.5, 0.5)

linear_values = linear(times)
cubic_values = cubic(times)

target_time = 5.0

print(f"Linear Estimate at Hour 5: {float(linear(target_time)):.2f} m")
print(f"Cubic Spline Estimate at Hour 5: {float(cubic(target_time)):.2f} m")

# Plot results
plt.scatter(hours, water_level, color="red", label="Measured Values")
plt.plot(times, linear_values, label="Linear Interpolation")
plt.plot(times, cubic_values, label="Cubic Spline")

plt.xlabel("Time (Hours)")
plt.ylabel("Water Level (m)")
plt.title("Reservoir Water-Level Interpolation")

plt.legend()
plt.grid(True)

plt.show()