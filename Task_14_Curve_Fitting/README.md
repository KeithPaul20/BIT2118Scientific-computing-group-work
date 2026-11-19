# Task 14: Curve Fitting and Approximation

## 1. Objective

To demonstrate how curve fitting can be used to model real-world data by finding a mathematical function that closely follows observed measurements. The task uses least-squares fitting to estimate the relationship between variables and make future predictions.

## 2. Concepts Covered

- Curve fitting.
- Least-squares approximation.
- Quadratic models.
- Prediction using fitted models.
- Root Mean Square Error (RMSE).
- Data visualization using Matplotlib.

## 3. Original Problem

A system administrator measures server response times under different user loads. The objective is to determine a mathematical model that describes the relationship between the number of users and the server response time.

### Input Data

Concurrent Users:

```text
[50, 100, 150, 200, 250, 300, 350]
```

Response Time (ms):

```text
[82, 95, 115, 145, 185, 238, 305]
```

### Mathematical Operations

1. Curve Fitting

A quadratic model is used:

```text
y = ax² + bx + c
```

2. Least-Squares Optimization

The model parameters are determined using:

```python
scipy.optimize.curve_fit()
```

3. Error Analysis

```text
RMSE = Root Mean Square Error
```

### Output Interpretation

The fitted curve approximates the relationship between server load and response time.

A low RMSE value indicates that the model closely matches the observed data.

The model can also be used to predict response times beyond the measured values.

## 4. Parameter Modification

The response time for 350 users was changed from:

```text
305 ms
```

to:

```text
340 ms
```

### Observed Changes

- The fitted curve became steeper.
- The predicted response times increased.
- The RMSE value changed.
- Future predictions produced larger estimates.

### Interpretation

Increasing one measurement affects the fitted model because curve fitting attempts to minimize the overall error between the model and all observations.

## 5. Related Real-World Application: Mobile Data Usage Growth Analysis

A telecommunications company wants to model how customer mobile data usage changes over time. Historical monthly data usage records are available, and management wants to forecast future demand.

### Input Data

Months:

```text
[1, 2, 3, 4, 5, 6, 7]
```

Data Usage (GB):

```text
[12, 15, 19, 24, 30, 38, 47]
```

### Assumptions

- Customer behavior remains relatively consistent.
- Historical usage data is accurate.
- No major pricing or policy changes occur during the forecast period.
- A quadratic model adequately describes the growth trend.

### Operations Performed

- Quadratic curve fitting.
- Model parameter estimation.
- RMSE calculation.
- Future usage prediction.
- Graphical visualization of observed and fitted data.

### Output Interpretation

The fitted curve represents the relationship between time and mobile data usage.

The predicted value for Month 10 provides an estimate of future data demand.

RMSE measures how accurately the model follows the observed usage data.

These results can help telecommunications companies plan network capacity and resource allocation.

## 6. Files

- `Task_14_curve_fitting.py` – Original server response-time modeling problem.
- `Task_14_real_world.py` – Mobile data usage growth analysis application.
- `README.md` – Documentation, assumptions, parameter modifications and interpretation.

## 7. Conclusion

This task demonstrated how curve fitting can be used to model relationships in real-world data and make predictions. By applying least-squares approximation, it was possible to estimate future trends from historical observations. The mobile data usage example showed how curve fitting supports forecasting and decision-making in modern communication networks.