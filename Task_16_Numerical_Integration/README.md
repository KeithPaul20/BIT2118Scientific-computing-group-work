# Task 16: Numerical Integration

## 1. Objective

To demonstrate how numerical integration can be used to estimate accumulated quantities from measured data. The task applies both the Trapezoidal Rule and Simpson's Rule to approximate the area under a curve and calculate total quantities.

## 2. Concepts Covered

- Numerical integration.
- Trapezoidal Rule.
- Simpson's Rule.
- Area under a curve.
- Accumulated quantities.
- Scientific data analysis.
- Data visualization using Matplotlib.

## 3. Original Problem

A smart electricity meter records power consumption at fixed time intervals throughout the day. The objective is to estimate the total energy consumed using numerical integration techniques.

### Input Data

Time (Hours):

```text
[0, 2, 4, 6, 8, 10, 12]
```

Power Consumption (kW):

```text
[0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9]
```

### Mathematical Operations

1. Trapezoidal Rule

Approximates the area under the curve using a series of trapezoids.

2. Simpson's Rule

Approximates the area under the curve using parabolic segments.

### Output Interpretation

The calculated area under the power-time graph represents the total electrical energy consumed during the measurement period.

Comparing the two methods helps evaluate the accuracy of the numerical approximation.

## 4. Parameter Modification

The power consumption at 6 hours was changed from:

```text
1.8 kW
```

to:

```text
2.2 kW
```

### Observed Changes

- Total energy consumption increased.
- Both integration methods produced larger estimates.
- The difference between the two methods changed slightly.

### Interpretation

Since numerical integration accumulates the area under the curve, increasing one power measurement increases the total estimated energy consumption.

## 5. Related Real-World Application: River Flow Monitoring

Environmental engineers monitor water flow in a river throughout the day. Measurements are collected at regular intervals, and the objective is to estimate the total volume of water that passed through a monitoring point.

### Input Data

Time (Hours):

```text
[0, 2, 4, 6, 8, 10, 12]
```

Flow Rate (m³/h):

```text
[45, 52, 67, 75, 70, 60, 50]
```

### Assumptions

- Flow-rate measurements are accurate.
- Measurements are collected at regular intervals.
- Water flow changes gradually between measurements.
- No extreme flooding or sudden flow changes occur during the observation period.

### Operations Performed

- Trapezoidal Rule integration.
- Simpson's Rule integration.
- Comparison of numerical integration methods.
- Visualization of river flow data.

### Output Interpretation

The calculated integral represents the total volume of water that flowed through the river during the measurement period.

Both numerical methods provide estimates of the accumulated water volume, with Simpson's Rule typically producing a more accurate result for smooth data.

These calculations assist environmental engineers in water-resource management and flood monitoring.

## 6. Files

- `Task_16_numerical_integration.py` – Original electrical energy consumption problem.
- `Task_16_real_world.py` – River flow monitoring application.
- `README.md` – Documentation, assumptions, parameter modifications and interpretation.

## 7. Conclusion

This task demonstrated how numerical integration can be used to estimate accumulated quantities when an exact mathematical expression is unavailable. By applying the Trapezoidal Rule and Simpson's Rule, it was possible to estimate total river water volume from discrete flow measurements. The example highlights the importance of numerical integration in environmental engineering, scientific analysis, and resource management.