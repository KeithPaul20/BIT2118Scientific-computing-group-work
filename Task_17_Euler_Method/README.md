# Task 17: Ordinary Differential Equations – Euler Method

## 1. Objective

To demonstrate how Euler's Method can be used to numerically solve ordinary differential equations (ODEs). The task shows how a quantity that changes over time can be approximated using small step-by-step calculations.

## 2. Concepts Covered

- Ordinary Differential Equations (ODEs).
- Euler Method.
- Numerical approximation.
- Step size and accuracy.
- Population growth modeling.
- Comparison of numerical and exact solutions.
- Data visualization using Matplotlib.

## 3. Original Problem

A hot object cools down according to Newton's Law of Cooling. The objective is to estimate the object's temperature over time using Euler's Method and compare the approximation with the exact analytical solution.

### Input Data

Ambient Temperature:

```text
25°C
```

Initial Temperature:

```text
90°C
```

Cooling Constant:

```text
0.12
```

Step Size:

```text
1 minute
```

Simulation Duration:

```text
30 minutes
```

### Mathematical Operations

Newton's Law of Cooling:

```text
dT/dt = -k(T - Tambient)
```

Euler Update Formula:

```text
T(n+1) = T(n) + h × f(Tn)
```

### Output Interpretation

The numerical solution estimates the object's temperature at each time step.

Comparison with the exact solution allows the approximation error to be evaluated.

## 4. Parameter Modification

The cooling constant was changed from:

```text
0.12
```

to:

```text
0.20
```

### Observed Changes

- The object cooled more rapidly.
- Final temperature decreased.
- The Euler approximation reached ambient temperature more quickly.

### Interpretation

A larger cooling constant increases the rate at which heat is lost to the environment, causing faster cooling.

## 5. Related Real-World Application: Population Growth Modeling

A wildlife conservation agency wants to estimate the growth of an animal population over time. The population grows continuously at a fixed percentage rate each year.

### Input Data

Initial Population:

```text
500 animals
```

Growth Rate:

```text
8% per year
```

Step Size:

```text
1 year
```

Simulation Period:

```text
20 years
```

### Assumptions

- The growth rate remains constant.
- There are sufficient resources to support population growth.
- No migration occurs.
- Environmental conditions remain stable.

### Operations Performed

- Application of Euler's Method.
- Numerical estimation of population growth.
- Comparison with the exact exponential growth model.
- Calculation of approximation error.
- Visualization of population growth over time.

### Output Interpretation

The numerical solution estimates the population size at each year.

The exact solution provides a benchmark for comparison.

The difference between the two solutions represents the numerical error introduced by Euler's Method.

The graph illustrates how the population changes over time and how closely the approximation follows the exact model.

## 6. Files

- `Task_17_euler_ode.py` – Original cooling problem.
- `Task_17_real_world.py` – Population growth modeling application.
- `README.md` – Documentation, assumptions, parameter modifications and interpretation.

## 7. Conclusion

This task demonstrated how Euler's Method can be used to approximate solutions to ordinary differential equations. By applying the method to a population growth model, it was possible to estimate future population sizes using simple numerical calculations. The comparison with the exact solution illustrated both the usefulness and limitations of numerical approximation methods in scientific computing.