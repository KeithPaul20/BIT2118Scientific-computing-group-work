# Task 06: Solution of Systems of Linear Equations

## 1. Objective

To demonstrate how systems of linear equations can be represented in matrix form and solved using NumPy. This task shows how unknown quantities can be determined from known resource constraints.

## 2. Concepts Covered

- Systems of linear equations.
- Matrix representation of equations.
- Solving equations using `np.linalg.solve()`.
- Verification of solutions through matrix multiplication.
- Real-world resource allocation problems.

## 3. Original Problem

A company operates two types of servers. Each server type consumes different amounts of CPU and memory resources. Given the total CPU and memory usage, the objective is to determine how many servers of each type are currently active.

### Input Data

Coefficient Matrix:

```text
[4  2]
[8 12]
```

Resource Vector:

```text
[20 72]
```

### Mathematical Operations

The system is represented as:

```text
AX = B
```

where:

- A = coefficient matrix
- X = unknown server quantities
- B = observed resource usage

The solution is obtained using:

```python
np.linalg.solve(A, b)
```

### Output Interpretation

The solution provides the number of active Type A and Type B servers. Verification confirms that the calculated values satisfy both equations.

## 4. Parameter Modification

The original memory usage was changed from:

```text
72 GB
```

to:

```text
80 GB
```

### Observed Changes

- The number of Type A servers decreased.
- The number of Type B servers increased.
- The overall solution changed to satisfy the new memory requirement.

### Interpretation

Changing one resource constraint affects the entire solution because all equations are interconnected. Increasing memory demand requires a different combination of servers.

## 5. Related Real-World Application: Manufacturing Production Planning

A manufacturing company produces two products using labour hours and machine hours. Management knows the total resources consumed but needs to determine how many units of each product were produced.

### Input Data

Labour Hours Equation:

```text
3x + 2y = 120
```

Machine Hours Equation:

```text
4x + 5y = 220
```

where:

- x = Product A units
- y = Product B units

### Assumptions

- All labour hours are fully utilized.
- All machine hours are fully utilized.
- Production data is accurate.
- Both products require fixed resource amounts per unit.

### Operations Performed

- Construction of a coefficient matrix.
- Representation of resource totals as a vector.
- Solving the linear system using `np.linalg.solve()`.
- Verification using matrix multiplication.

### Output Interpretation

The solution determines the exact number of Product A and Product B units that satisfy both labour and machine hour constraints.

The verification step confirms that the solution accurately reproduces the known resource totals.

## 6. Files

- `Task_06_linear_systems.py` – Original server resource allocation problem.
- `Task_06_real_world.py` – Manufacturing production planning application.
- `README.md` – Documentation, assumptions, parameter modifications and interpretation.

## 7. Conclusion

This task demonstrated how systems of linear equations can be used to solve practical resource allocation problems. Matrix methods provide an efficient and reliable way to determine unknown quantities in engineering, manufacturing, economics and scientific computing applications.