import numpy as np

# GPS Distance Accuracy Analysis

true_distance = 125.678954
gps_distance = 125.679000

absolute_error = abs(true_distance - gps_distance)
relative_error = absolute_error / abs(true_distance)

print(f"True Distance: {true_distance:.6f} m")
print(f"GPS Distance: {gps_distance:.6f} m")

print(f"Absolute Error: {absolute_error:.8f} m")
print(f"Relative Error: {relative_error:.8%}")

# Floating-point representation example
calculated = 0.1 + 0.2
expected = 0.3

print("\nFloating-Point Comparison:")
print(f"0.1 + 0.2 = {calculated}")
print("Exact Comparison:", calculated == expected)
print("Tolerance Comparison:", np.isclose(calculated, expected))