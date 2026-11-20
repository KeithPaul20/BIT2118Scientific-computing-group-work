# Task 04: Floating-Point Arithmetic and Numerical Errors

## 1. Objective

To demonstrate how numerical errors occur in computer calculations due to the finite precision of floating-point representation. The task also shows how error measurements can be used to evaluate computational accuracy.

## 2. Concepts Covered

- Floating-point representation of real numbers.
- Round-off errors.
- Absolute error.
- Relative error.
- Exact and tolerance-based comparisons.
- Numerical accuracy in scientific computing.

## 3. Original Problem

A program investigates the floating-point arithmetic issue where:

```text
0.1 + 0.2 ≠ 0.3
```

when compared using exact equality in a computer.

The program also calculates absolute and relative errors by comparing an approximate value of √2 with its true value.

### Input Data

Values:

```text
0.1
0.2
0.3
```

True Value:

```text
√2
```

Approximate Value:

```text
1.414
```

### Mathematical Operations

1. Floating-Point Comparison

```python
calculated == expected
```

2. Tolerance-Based Comparison

```python
np.isclose()
```

3. Absolute Error

```text
|True Value − Approximate Value|
```

4. Relative Error

```text
Absolute Error / True Value
```

### Output Interpretation

The program demonstrates that decimal numbers cannot always be represented exactly inside a computer.

The absolute and relative errors quantify the difference between the true value and the approximation.

The tolerance comparison shows a more reliable way of comparing floating-point values.

## 4. Parameter Modification

The approximate value of √2 was changed from:

```text
1.414
```

to:

```text
1.415
```

### Observed Changes

- Absolute error increased.
- Relative error increased.
- Floating-point comparison results remained unchanged.

### Interpretation

Using a less accurate approximation increases numerical error. This demonstrates the importance of precision in scientific calculations.

## 5. Related Real-World Application: GPS Distance Accuracy Analysis

GPS devices use floating-point calculations to estimate distances between locations. Due to rounding and approximation errors, the measured value may differ slightly from the actual distance.

### Input Data

True Distance:

```text
125.678954 m
```

GPS Distance:

```text
125.679000 m
```

### Assumptions

- The true distance is measured accurately.
- GPS readings contain small numerical errors.
- Calculations are performed using standard floating-point arithmetic.

### Operations Performed

- Absolute error calculation.
- Relative error calculation.
- Floating-point comparison.
- Tolerance-based validation.

### Output Interpretation

The absolute error measures the difference between the true distance and the GPS reading.

The relative error indicates the size of the error relative to the actual distance.

Small numerical errors are generally acceptable, but they can accumulate in large-scale navigation systems.

The tolerance comparison helps verify whether two values are effectively equal despite minor rounding differences.

## 6. Files

- `Task_04_numerical_errors.py` – Original floating-point arithmetic problem.
- `Task_04_real_world.py` – GPS distance accuracy analysis application.
- `README.md` – Documentation, assumptions, parameter modifications and interpretation.

## 7. Conclusion

This task demonstrated how floating-point arithmetic can introduce small numerical errors in computer calculations. Through error analysis and tolerance-based comparisons, it is possible to measure and manage these inaccuracies effectively. The GPS distance example illustrated the practical importance of understanding floating-point behavior in scientific and engineering applications.