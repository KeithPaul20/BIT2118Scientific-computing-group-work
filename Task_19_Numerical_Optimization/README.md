# Task 19: Numerical Optimization

## 1. Objective

To demonstrate how optimization techniques can be used to find the best solution to a problem while satisfying given constraints. The task applies numerical optimization to minimize cost while meeting operational requirements.

## 2. Concepts Covered

- Numerical optimization.
- Objective functions.
- Constraints.
- Feasible solutions.
- Cost minimization.
- SciPy optimization using `minimize()`.
- Resource allocation.

## 3. Original Problem

A cloud service provider operates two types of servers. Each server type has a different operating cost and processing capacity. The objective is to determine the least expensive server allocation capable of meeting a minimum processing capacity requirement.

### Input Data

Server Costs:

```text
Type A = 12 units
Type B = 18 units
```

Processing Capacity:

```text
Type A = 100 units
Type B = 170 units
```

Required Capacity:

```text
1000 units
```

### Mathematical Operations

Objective Function:

```text
Cost = 12x + 18y
```

Constraint:

```text
100x + 170y ≥ 1000
```

Optimization Method:

```python
scipy.optimize.minimize()
```

### Output Interpretation

The optimal solution provides the server allocation that achieves the required processing capacity at the lowest possible cost.

## 4. Parameter Modification

The minimum required capacity was changed from:

```text
1000 units
```

to:

```text
1200 units
```

### Observed Changes

- More server resources were required.
- Total cost increased.
- The optimal allocation shifted toward higher-capacity solutions.

### Interpretation

Increasing the required capacity reduces the number of feasible solutions and generally increases the minimum operating cost.

## 5. Related Real-World Application: Delivery Fleet Cost Optimization

A logistics company operates a fleet of delivery vehicles. Management wants to determine the cheapest combination of trucks that can deliver at least 5,000 kg of goods per day.

### Input Data

Operating Costs:

```text
Small Truck = KES 8,000
Large Truck = KES 12,000
```

Delivery Capacities:

```text
Small Truck = 500 kg
Large Truck = 900 kg
```

Required Delivery Capacity:

```text
5,000 kg
```

### Assumptions

- All trucks are available for use.
- Operating costs remain constant.
- Every truck operates at its full capacity.
- Delivery demand is at least 5,000 kg per day.

### Operations Performed

- Definition of an objective function.
- Definition of capacity constraints.
- Cost minimization using SciPy optimization.
- Integer solution verification.
- Graphical visualization of feasible solutions.

### Output Interpretation

The optimized truck allocation represents the least expensive delivery plan capable of satisfying the required delivery capacity.

The minimum operating cost helps management allocate resources efficiently.

The graph illustrates the constraint boundary and the combinations of trucks that satisfy operational requirements.

## 6. Files

- `Task_19_optimization.py` – Original cloud resource allocation problem.
- `Task_19_real_world.py` – Delivery fleet cost optimization application.
- `README.md` – Documentation, assumptions, parameter modifications and interpretation.

## 7. Conclusion

This task demonstrated how numerical optimization can be used to solve practical resource allocation problems. By minimizing costs while meeting operational requirements, optimization techniques support better decision-making in logistics, business planning, engineering, and scientific computing. The delivery fleet example showed how optimization can improve efficiency and reduce expenses in real-world operations.