# Task 15: Numerical Differentiation

## 1. Objective

To demonstrate how numerical differentiation can be used to estimate rates of change from measured data when an analytical derivative is unavailable. The task applies finite difference methods to approximate derivatives using observed values.

## 2. Concepts Covered

- Numerical differentiation.
- Forward difference method.
- Central difference method.
- Backward difference method.
- Rate of change estimation.
- Data visualization using Matplotlib.

## 3. Original Problem

A GPS device records the position of a vehicle at regular time intervals. The objective is to estimate the vehicle's speed using numerical differentiation.

### Input Data

Time (s):

```text
[0, 1, 2, 3, 4, 5, 6]
```

Position (m):

```text
[0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0]
```

### Mathematical Operations

1. Forward Difference

```text
f'(x) ≈ [f(x+h) - f(x)] / h
```

2. Central Difference

```text
f'(x) ≈ [f(x+h) - f(x-h)] / 2h
```

3. Backward Difference

```text
f'(x) ≈ [f(x) - f(x-h)] / h
```

### Output Interpretation

The estimated derivative values represent the speed of the vehicle at different points in time.

The graph shows how speed changes throughout the journey.

## 4. Parameter Modification

The position recorded at 5 seconds was changed from:

```text
30.0 m
```

to:

```text
32.0 m
```

### Observed Changes

- The estimated speed near 5 seconds increased.
- The shape of the speed graph changed.
- Central difference calculations around the modified point produced higher values.

### Interpretation

Numerical differentiation is sensitive to changes in data values. Modifying a single measurement affects nearby derivative estimates because they depend on neighboring observations.

## 5. Related Real-World Application: Vehicle Fuel Consumption Analysis

A transport company monitors the cumulative fuel consumed by a vehicle throughout a journey. Engineers need to estimate the instantaneous fuel consumption rate at different times.

### Input Data

Time (Hours):

```text
[0, 1, 2, 3, 4, 5, 6]
```

Fuel Used (Liters):

```text
[0.0, 2.5, 5.8, 9.6, 14.0, 19.0, 25.0]
```

### Assumptions

- Fuel measurements are accurate.
- Fuel consumption changes gradually over time.
- Measurements are recorded at equal time intervals.
- External factors such as road conditions are ignored.

### Operations Performed

- Forward difference approximation.
- Central difference approximation.
- Backward difference approximation.
- Graphical visualization of fuel consumption rate.

### Output Interpretation

The calculated derivative values represent the rate at which fuel is being consumed at different times during the journey.

Higher values indicate periods of increased fuel usage, while lower values indicate more efficient operation.

The graph helps identify trends and changes in fuel consumption patterns.

## 6. Files

- `Task_15_numerical_differentiation.py` – Original GPS speed estimation problem.
- `Task_15_real_world.py` – Vehicle fuel consumption analysis application.
- `README.md` – Documentation, assumptions, parameter modifications and interpretation.

## 7. Conclusion

This task demonstrated how numerical differentiation can be used to estimate rates of change from measured data. By applying finite difference methods, it was possible to determine fuel consumption rates from cumulative fuel measurements. The example illustrates the importance of numerical differentiation in engineering, transportation, scientific analysis, and performance monitoring.