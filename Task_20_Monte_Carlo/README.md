# Task 20: Random Numbers and Monte Carlo Methods

## 1. Objective

To demonstrate how random number generation and Monte Carlo simulation can be used to estimate probabilities and analyze uncertainty in real-world systems.

## 2. Concepts Covered

- Random number generation.
- Probability estimation.
- Monte Carlo simulation.
- Risk analysis.
- Statistical convergence.
- Simulation of uncertain events.
- Data visualization using Matplotlib.

## 3. Original Problem

A network administrator wants to estimate the probability that a server becomes overloaded when customer demand varies unpredictably.

Instead of calculating the probability analytically, Monte Carlo simulation is used to generate thousands of possible demand scenarios and estimate the probability experimentally.

### Input Data

Server Capacity:

```text
1000 units
```

Mean Demand:

```text
850 units
```

Standard Deviation:

```text
120 units
```

Number of Simulations:

```text
100,000
```

### Mathematical Operations

1. Random Demand Generation

```python
rng.normal()
```

2. Overload Detection

```text
Demand > Capacity
```

3. Probability Estimation

```text
Probability = Overloaded Cases / Total Simulations
```

### Output Interpretation

The estimated probability represents the likelihood that customer demand exceeds server capacity.

The convergence graph demonstrates how the estimate becomes more stable as the number of simulations increases.

## 4. Parameter Modification

The server capacity was changed from:

```text
1000 units
```

to:

```text
900 units
```

### Observed Changes

- The overload probability increased significantly.
- More simulations exceeded the capacity limit.
- The risk of service disruption became higher.

### Interpretation

Reducing server capacity increases the likelihood of overload. Monte Carlo simulations help quantify this risk before changes are implemented.

## 5. Related Real-World Application: Hospital Emergency Room Capacity Planning

Hospitals often experience unpredictable numbers of emergency patients each day. Management wants to estimate the probability that patient arrivals exceed the hospital's treatment capacity.

### Input Data

Emergency Room Capacity:

```text
50 patients per day
```

Average Daily Patients:

```text
42 patients
```

Standard Deviation:

```text
8 patients
```

Number of Simulations:

```text
100,000
```

### Assumptions

- Daily patient arrivals follow a normal distribution.
- Historical data accurately reflects patient arrival patterns.
- Hospital capacity remains constant.
- External emergency events are not considered.

### Operations Performed

- Random generation of patient arrival scenarios.
- Detection of overload conditions.
- Probability estimation using Monte Carlo simulation.
- Running probability calculation to observe convergence.
- Graphical visualization of probability stabilization.

### Output Interpretation

The estimated probability represents the likelihood that the emergency room receives more patients than it can handle in a day.

A higher probability indicates a greater risk of overcrowding and longer waiting times.

The convergence graph demonstrates how simulation results become increasingly reliable as more random samples are generated.

## 6. Files

- `Task_20_monte_carlo.py` – Original server overload probability problem.
- `Task_20_real_world.py` – Hospital emergency room capacity planning application.
- `README.md` – Documentation, assumptions, parameter modifications and interpretation.

## 7. Conclusion

This task demonstrated how Monte Carlo simulation can be used to estimate probabilities in situations involving uncertainty. By generating a large number of random scenarios, complex risks can be approximated without requiring exact analytical solutions. The hospital capacity planning example illustrates how Monte Carlo methods support decision-making in healthcare, engineering, finance, and scientific research.