import numpy as np
from scipy.optimize import root

# Bridge Design Analysis
# Determine the intersection between a cable profile
# and a support structure

# Cable: y = x² - 2
# Support structure: x² + y² = 9

def equations(z):
    x, y = z

    return [
        x**2 + y**2 - 9,
        y - (x**2 - 2)
    ]

initial_guesses = [
    [1.5, 1.0],
    [-1.5, 1.0]
]

for guess in initial_guesses:
    solution = root(equations, guess)

    print("Initial Guess:", guess)
    print("Intersection Point:", solution.x)
    print("Residuals:", equations(solution.x))
    print("Converged:", solution.success)
    print()
