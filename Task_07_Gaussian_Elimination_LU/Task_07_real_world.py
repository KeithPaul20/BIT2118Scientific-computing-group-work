import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Water distribution network

A = np.array([
    [6, -2, 0],
    [-2, 6, -2],
    [0, -2, 5]
])

demand_sets = [
    np.array([120, 90, 80]),
    np.array([130, 100, 85]),
    np.array([125, 95, 82])
]

# Perform LU decomposition once
lu, piv = lu_factor(A)

for i, demand in enumerate(demand_sets, start=1):
    flow = lu_solve((lu, piv), demand)

    residual = demand - A @ flow

    print(f"\nDemand Set {i}")
    print("Flow Solution:", flow)
    print("Residual Norm:", np.linalg.norm(residual))