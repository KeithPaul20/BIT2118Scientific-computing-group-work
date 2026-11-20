# Task 18: Numerical Solution of ODEs Using SciPy

## 1. Objective

To demonstrate how SciPy's ODE solver can be used to numerically solve ordinary differential equations. The task shows how dynamic systems can be modeled and analyzed without manually implementing numerical algorithms.

## 2. Concepts Covered

- Ordinary Differential Equations (ODEs).
- Numerical solution of ODEs.
- SciPy `solve_ivp()`.
- Dynamic system modeling.
- Comparison between numerical and analytical solutions.
- Data visualization using Matplotlib.

## 3. Original Problem

An RC (Resistor-Capacitor) circuit is charging over time. The objective is to model the voltage across the capacitor using SciPy's ODE solver and compare the numerical solution with the exact analytical solution.

### Input Data

Supply Voltage:

```text
5.0 V
```

Resistance:

```text
1000 Ω
```

Capacitance:

```text
0.001 F
```

Initial Voltage:

```text
0 V
```

Time Interval:

```text
0 to 5 seconds
```

### Mathematical Operations

RC Circuit Differential Equation:

```text
dV/dt = (Vs - V)/(RC)
```

Numerical Solution:

```python
solve_ivp()
```

Exact Solution:

```text
V(t) = Vs(1 - e^(-t/RC))
```

### Output Interpretation

The numerical solution represents the capacitor voltage at various time intervals.

The exact solution is used to verify the accuracy of the solver.

## 4. Parameter Modification

The capacitance value was changed from:

```text
0.001 F
```

to:

```text
0.002 F
```

### Observed Changes

- The capacitor charged more slowly.
- The final voltage at a given time decreased.
- The charging curve became less steep.

### Interpretation

Increasing capacitance increases the circuit time constant (RC), causing the capacitor to require more time to reach its steady-state voltage.

## 5. Related Real-World Application: Drug Elimination from the Bloodstream

Medical researchers often model how the concentration of a drug decreases in a patient's bloodstream after administration. Differential equations can be used to describe the rate at which the body removes the drug.

### Input Data

Initial Drug Concentration:

```text
100 mg/L
```

Elimination Rate Constant:

```text
0.25 per hour
```

Time Interval:

```text
0 to 12 hours
```

### Assumptions

- Drug elimination follows first-order kinetics.
- The elimination rate remains constant.
- No additional doses are administered.
- Patient conditions remain unchanged during the observation period.

### Operations Performed

- Formulation of the drug elimination ODE.
- Numerical solution using `solve_ivp()`.
- Calculation of the exact analytical solution.
- Error analysis between numerical and exact results.
- Graphical visualization of concentration changes over time.

### Mathematical Model

Drug elimination is represented as:

```text
dC/dt = -kC
```

where:

- C = Drug concentration
- k = Elimination rate constant

### Output Interpretation

The numerical solution shows how the drug concentration decreases over time.

The graph illustrates the exponential decay of the drug in the bloodstream.

The maximum error measures the difference between the numerical solution and the exact analytical solution, confirming the accuracy of the solver.

## 6. Files

- `Task_18_scipy_ode.py` – Original RC circuit charging problem.
- `Task_18_real_world.py` – Drug elimination modeling application.
- `README.md` – Documentation, assumptions, parameter modifications and interpretation.

## 7. Conclusion

This task demonstrated how SciPy's ODE solver can efficiently solve differential equations that arise in real-world applications. The drug elimination model showed how numerical methods can be used to analyze biological processes and predict system behavior over time. The comparison with the exact solution confirmed the accuracy and reliability of the numerical approach.