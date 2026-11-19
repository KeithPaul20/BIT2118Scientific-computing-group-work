# Task 10: Root Finding Using Bisection and Fixed-Point Methods

## 1. Objective

To demonstrate how numerical root-finding methods can be used to determine unknown values that satisfy nonlinear equations. This task applies both the Bisection Method and Fixed-Point Iteration to find an equilibrium solution.

## 2. Concepts Covered

- Nonlinear equations.
- Root finding.
- Bisection Method.
- Fixed-Point Iteration.
- Convergence of numerical methods.
- Graphical interpretation of roots.

## 3. Original Problem

A heat-transfer system is modeled using a nonlinear heat-balance equation. The goal is to determine the temperature at which heat gain becomes equal to heat loss.

### Input Data

Heat-Balance Equation:

```text
f(T) = T - 25 - 10e^(-T/20)
```

Initial Bisection Interval:

```text
[20, 40]
```

Initial Fixed-Point Guess:

```text
30°C
```

### Mathematical Operations

1. Bisection Method

Repeatedly divide the interval in half until the root is identified.

2. Fixed-Point Iteration

Transform the equation into:

```text
T = 25 + 10e^(-T/20)
```

and repeatedly evaluate:

```text
T(n+1) = g(Tn)
```

### Output Interpretation

The root represents the equilibrium temperature where heat gain equals heat loss. Both numerical methods should converge to approximately the same solution.

## 4. Parameter Modification

The initial interval for the Bisection Method was changed from:

```text
[20, 40]
```

to:

```text
[10, 30]
```

### Observed Changes

- The root remained unchanged.
- The number of iterations increased slightly.
- The convergence process took longer.

### Interpretation

The Bisection Method will always converge provided a valid interval containing a root is selected. Different intervals may require different numbers of iterations.

## 5. Related Real-World Application: Reservoir Water-Level Control

A reservoir receives water through an inlet channel and loses water through controlled outflow. Engineers need to determine the equilibrium water level where inflow and outflow are balanced.

### Input Data

Water-Balance Equation:

```text
f(h) = h - 10 - 5e^(-h/8)
```

Initial Bisection Interval:

```text
[10, 20]
```

Initial Fixed-Point Guess:

```text
15 m
```

### Assumptions

- Water inflow remains constant.
- Outflow behavior follows the given mathematical model.
- Environmental influences such as evaporation are ignored.
- The system eventually reaches equilibrium.

### Operations Performed

- Bisection Method root calculation.
- Fixed-Point Iteration.
- Convergence analysis.
- Graphical visualization of the equilibrium point.

### Output Interpretation

The calculated root represents the equilibrium water level of the reservoir.

When the function value becomes zero:

```text
Water Inflow = Water Outflow
```

The graph shows where the water-balance function intersects the horizontal axis, indicating the equilibrium condition.

## 6. Files

- `Task_10_bisection_fixed_point.py` – Original heat-balance problem.
- `Task_10_real_world.py` – Reservoir water-level control application.
- `README.md` – Documentation, assumptions, parameter modifications and interpretation.

## 7. Conclusion

This task demonstrated how numerical methods can be used to solve nonlinear equations that may not have simple analytical solutions. The Bisection Method and Fixed-Point Iteration both successfully identified the equilibrium water level, illustrating their usefulness in engineering, environmental management and scientific computing applications.