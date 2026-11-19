# Task 05: Matrix Algebra and Matrix Operations

## 1. Objective

To demonstrate how matrices can be used to organize data and perform transformations through matrix multiplication and determinant calculations.

## 2. Concepts Covered

- Matrix representation of numerical data.
- Matrix multiplication.
- Transformation matrices.
- Determinant calculation using NumPy.
- Real-world applications of matrix operations.

## 3. Original Problem

A graphics program needs to rotate and scale a set of two-dimensional coordinates representing points on an object. Matrix multiplication is used to apply the transformations efficiently and consistently.

### Input Data

- Coordinates of four points representing a square.
- Rotation matrix (45° rotation).
- Scaling matrix.

### Mathematical Operations

- Matrix multiplication.
- Matrix transformation.
- Determinant calculation.

### Output Interpretation

The program generates a new set of coordinates after scaling and rotation. The determinant indicates how the transformation changes the size of the object.

## 4. Parameter Modification

The original scaling factors were:

```text
x-direction = 2.0
y-direction = 1.5
```

Modified scaling factors:

```text
x-direction = 3.0
y-direction = 2.0
```

### Observed Changes

- The transformed coordinates became larger.
- The determinant of the transformation matrix increased.
- The object occupied a larger area after transformation.

### Interpretation

Increasing the scaling factors causes greater enlargement of the transformed object. Matrix transformations directly affect the resulting coordinates.

## 5. Related Real-World Application: Sales Growth Projection

A company wants to estimate future sales for two product categories across three regional branches.

### Input Data

Sales Matrix

[
[150000, 120000],
[180000, 140000],
[210000, 170000]
]

Growth Matrix

[
[1.12, 0],
[0, 1.08]
]

### Assumptions

- Product A sales are expected to increase by 12%.
- Product B sales are expected to increase by 8%.
- Growth rates remain constant during the projection period.

### Operations Performed

- Matrix multiplication.
- Determinant calculation.

### Output Interpretation

The projected sales matrix shows expected future revenue after applying growth rates to both products. The determinant indicates the overall scaling effect of the growth matrix.

## 6. Files

- `Task_05_matrix_algebra.py` – Original graphics transformation problem.
- `Task_05_Real_World.py` – Sales growth projection application.
- `README.md` – Documentation, assumptions and interpretation.

## 7. Conclusion

This task demonstrated how matrix algebra can be applied to solve practical business problems. Matrix multiplication provides an efficient way to perform large-scale calculations and projections in a structured manner.