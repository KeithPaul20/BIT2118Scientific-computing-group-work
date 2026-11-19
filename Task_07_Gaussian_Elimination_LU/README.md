# Task 07: Gaussian Elimination and LU Decomposition

## 1. Objective

To demonstrate how Gaussian Elimination and LU Decomposition can be used to efficiently solve systems of linear equations, especially when the same coefficient matrix is used repeatedly with different input values.

## 2. Concepts Covered

- Gaussian Elimination.
- LU Decomposition.
- Matrix factorization.
- Solving systems of linear equations.
- Residual error analysis.
- Reusing matrix decompositions for computational efficiency.

## 3. Original Problem

A simulation system uses the same coefficient matrix repeatedly but receives different measurement vectors over time. Solving each system from scratch would be computationally expensive.

LU Decomposition is used to factor the coefficient matrix once and then reuse the factorization for multiple measurement vectors.

### Input Data

Coefficient Matrix:

```text
[ 4  -1   0 ]
[-1   4  -1 ]
[ 0  -1   3 ]
```

Measurement Vectors:

```text
[15, 10, 10]
[16, 11,  9]
[14, 12, 11]
```

### Mathematical Operations

1. LU Decomposition

```text
A = LU
```

2. Solving Linear Systems

```text
Ax = b
```

3. Residual Calculation

```text
Residual = b - Ax
```

### Output Interpretation

The solution vector represents the unknown values that satisfy each system of equations. The residual norm measures the accuracy of the solution.

## 4. Parameter Modification

The first measurement vector:

```text
[15, 10, 10]
```

was modified to:

```text
[18, 12, 11]
```

### Observed Changes

- The solution values increased.
- The residual norm remained close to zero.
- The coefficient matrix remained unchanged.

### Interpretation

Changing the measurement values changes the system solution. Since the matrix remains the same, LU Decomposition can be reused, reducing computational effort.

## 5. Related Real-World Application: Water Distribution Network

A city water authority manages a network of interconnected pipelines supplying water to three residential zones. The relationships between the pipelines remain fixed, but water demand changes throughout the day.

### Input Data

Pipeline Coefficient Matrix

```text
[ 6  -2   0 ]
[-2   6  -2 ]
[ 0  -2   5 ]
```

Water Demand Vectors

```text
[120, 90, 80]
[130,100,85]
[125,95,82]
```

### Assumptions

- Pipeline characteristics remain constant.
- Water demand varies throughout the day.
- Flow losses are negligible.
- Measurements are accurate.

### Operations Performed

- LU Decomposition of the coefficient matrix.
- Solving multiple systems using the same LU factors.
- Calculating residual errors for validation.

### Output Interpretation

The solution vector represents the amount of water flow required in each section of the network to satisfy demand.

The residual norm indicates whether the computed solution accurately satisfies the equations.

Using LU Decomposition improves efficiency because the matrix factorization is performed only once.

## 6. Files

- `Task_07_gaussian_lu.py` – Original simulation problem.
- `Task_07_real_world.py` – Water distribution network application.
- `README.md` – Documentation, assumptions, parameter modifications and interpretation.

## 7. Conclusion

This task demonstrated how Gaussian Elimination and LU Decomposition can efficiently solve repeated systems of linear equations. The water distribution example showed a practical use of matrix factorization in engineering systems where demand changes but system structure remains constant.