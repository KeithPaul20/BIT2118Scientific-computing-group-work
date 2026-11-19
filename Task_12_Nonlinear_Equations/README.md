# Task 12: Polynomial and Nonlinear Equation Solving

## 1. Objective

To demonstrate how numerical methods can be used to solve nonlinear equations and determine unknown values that satisfy multiple mathematical conditions simultaneously.

## 2. Concepts Covered

- Polynomial equations.
- Nonlinear equations.
- Systems of nonlinear equations.
- Numerical root finding using SciPy.
- Equation residual analysis.
- Verification of numerical solutions.

## 3. Original Problem

The program determines the points of intersection between a circle and a parabola.

The equations are:

```text
Circle: x² + y² = 4
Parabola: y = x² - 1
```

Since the equations are nonlinear, numerical methods are used to find the solutions.

### Input Data

Circle Equation:

```text
x² + y² = 4
```

Parabola Equation:

```text
y = x² - 1
```

Initial Guess Values:

```text
[1, 1]
[-1, 1]
```

### Mathematical Operations

1. Formulation of nonlinear equations.

2. Numerical root finding using:

```python
scipy.optimize.root()
```

3. Residual calculation for validation.

### Output Interpretation

The solutions represent the coordinates where the circle and the parabola intersect.

Residual values close to zero indicate that the identified points satisfy both equations.

## 4. Parameter Modification

The circle radius was changed from:

```text
Radius = 2
```

to:

```text
Radius = 3
```

Modified equation:

```text
x² + y² = 9
```

### Observed Changes

- The intersection points shifted.
- The solution coordinates became larger.
- The solver still converged successfully.

### Interpretation

Increasing the radius changes the geometry of the problem, leading to different intersection locations between the two curves.

## 5. Related Real-World Application: Bridge Design Analysis

Civil engineers often need to determine where structural components intersect during bridge design.

In this example:

- A suspension cable is modeled by a parabola.
- A support structure is modeled by a circular arc.

The intersection points help engineers identify connection locations between components.

### Input Data

Cable Equation:

```text
y = x² - 2
```

Support Structure Equation:

```text
x² + y² = 9
```

Initial Guesses:

```text
[1.5, 1.0]
[-1.5, 1.0]
```

### Assumptions

- The bridge is analyzed using a two-dimensional model.
- The cable follows a perfect parabolic shape.
- The support structure forms a circular arc.
- Environmental loads are ignored.

### Operations Performed

- Construction of nonlinear equations.
- Numerical solution using SciPy's root solver.
- Residual analysis to validate solutions.

### Output Interpretation

The computed coordinates represent the locations where the suspension cable intersects the support structure.

These intersection points can be used during structural analysis and design verification.

Small residual values indicate accurate solutions.

## 6. Files

- `Task_12_nonlinear_equations.py` – Original circle and parabola intersection problem.
- `Task_12_real_world.py` – Bridge design analysis application.
- `README.md` – Documentation, assumptions, parameter modifications and interpretation.

## 7. Conclusion

This task demonstrated how numerical methods can solve systems of nonlinear equations that may be difficult or impossible to solve analytically. The bridge design example illustrated a practical engineering application where nonlinear equation solving helps determine important structural intersection points. The SciPy root solver efficiently identified accurate solutions and verified them through residual analysis.