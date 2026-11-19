# Task 13: Interpolation

## 1. Objective

To demonstrate how interpolation can be used to estimate unknown values between measured data points. The task uses both Linear Interpolation and Cubic Spline Interpolation to generate estimates from existing observations.

## 2. Concepts Covered

- Linear Interpolation.
- Cubic Spline Interpolation.
- Data estimation between known points.
- Numerical approximation.
- Curve visualization using Matplotlib.
- Scientific data analysis.

## 3. Original Problem

A temperature sensor records measurements every hour, but an application requires temperature estimates every 10 minutes.

Interpolation is used to estimate the missing values between the existing measurements.

### Input Data

Hours:

```text
[8, 9, 10, 11, 12, 13, 14]
```

Temperatures (°C):

```text
[18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0]
```

### Mathematical Operations

1. Linear Interpolation

Uses straight-line segments between neighboring points.

2. Cubic Spline Interpolation

Uses smooth cubic curves to estimate values.

### Output Interpretation

The estimated temperatures provide values at times where no measurements were recorded.

Linear interpolation produces straight-line estimates, while cubic splines generate smoother transitions between data points.

## 4. Parameter Modification

The temperature measurement at 12:00 was changed from:

```text
25.0°C
```

to:

```text
27.0°C
```

### Observed Changes

- The interpolated values near noon increased.
- The cubic spline curve became steeper.
- The estimated temperature at 10:30 also increased slightly.

### Interpretation

Interpolation depends on the surrounding data points. Changing one measurement influences nearby estimated values and alters the shape of the curve.

## 5. Related Real-World Application: Reservoir Water-Level Monitoring

A reservoir monitoring system records water levels every two hours. Engineers require water-level estimates every 30 minutes to improve monitoring and decision-making.

### Input Data

Time (Hours):

```text
[0, 2, 4, 6, 8, 10, 12]
```

Water Level (m):

```text
[3.5, 4.1, 5.2, 6.0, 5.8, 5.0, 4.2]
```

### Assumptions

- Water-level measurements are accurate.
- Changes in water level occur gradually.
- No sudden flooding or water releases occur during the monitoring period.
- Interpolation is sufficient for estimating missing values.

### Operations Performed

- Linear interpolation.
- Cubic spline interpolation.
- Estimation of water levels at intermediate times.
- Graphical visualization of measured and estimated values.

### Output Interpretation

The interpolated values provide estimated reservoir levels during periods when measurements are unavailable.

Linear interpolation gives simple estimates, while cubic spline interpolation provides a smoother representation of water-level changes over time.

These estimates can assist engineers in monitoring trends and managing water resources effectively.

## 6. Files

- `Task_13_interpolation.py` – Original temperature interpolation problem.
- `Task_13_real_world.py` – Reservoir water-level monitoring application.
- `README.md` – Documentation, assumptions, parameter modifications and interpretation.

## 7. Conclusion

This task demonstrated how interpolation can be used to estimate unknown values between measured observations. Both Linear Interpolation and Cubic Spline Interpolation successfully generated intermediate values from the available data. The reservoir monitoring example illustrated a practical application of interpolation in environmental and engineering systems where measurements may not always be available at the desired frequency.