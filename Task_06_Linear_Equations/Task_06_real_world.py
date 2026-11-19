import numpy as np

# Manufacturing production planning

# x = Units of Product A
# y = Units of Product B

# Labour hours equation
# 3x + 2y = 120

# Machine hours equation
# 4x + 5y = 220

A = np.array([
    [3, 2],
    [4, 5]
])

b = np.array([120, 220])

solution = np.linalg.solve(A, b)

product_a = solution[0]
product_b = solution[1]

verification = A @ solution

print(f"Product A Units: {product_a:.2f}")
print(f"Product B Units: {product_b:.2f}")

print("\nVerification:")
print(verification)