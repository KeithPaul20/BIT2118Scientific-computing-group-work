import numpy as np

sales = np.array([
    [150000, 120000],
    [180000, 140000],
    [210000, 170000]
])

growth_matrix = np.array([
    [1.12, 0],
    [0, 1.08]
])

projected_sales = sales @ growth_matrix

determinant = np.linalg.det(growth_matrix)

print("Current Sales:")
print(sales)

print("\nProjected Sales:")
print(projected_sales)

print(f"\nDeterminant: {determinant:.4f}")