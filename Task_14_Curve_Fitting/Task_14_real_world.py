import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Mobile Data Usage Growth Analysis

months = np.array([1, 2, 3, 4, 5, 6, 7], dtype=float)

data_usage = np.array([
    12, 15, 19, 24, 30, 38, 47
], dtype=float)

# Quadratic model
def model(x, a, b, c):
    return a * x**2 + b * x + c

# Fit curve
parameters, covariance = curve_fit(
    model,
    months,
    data_usage
)

a, b, c = parameters

predicted = model(months, a, b, c)

rmse = np.sqrt(
    np.mean((data_usage - predicted) ** 2)
)

future_month = 10
future_usage = model(future_month, a, b, c)

print(f"Fitted Model:")
print(f"y = {a:.4f}x² + {b:.4f}x + {c:.4f}")

print(f"\nRMSE: {rmse:.4f} GB")

print(
    f"Predicted Data Usage in Month {future_month}: "
    f"{future_usage:.2f} GB"
)

# Plot
x_plot = np.linspace(1, 10, 300)

plt.scatter(
    months,
    data_usage,
    color="red",
    label="Observed Data"
)

plt.plot(
    x_plot,
    model(x_plot, a, b, c),
    label="Fitted Curve"
)

plt.xlabel("Month")
plt.ylabel("Data Usage (GB)")
plt.title("Mobile Data Usage Growth")

plt.legend()
plt.grid(True)

plt.show()