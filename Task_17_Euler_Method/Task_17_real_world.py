import numpy as np
import matplotlib.pyplot as plt

# Population Growth Using Euler Method

initial_population = 500

growth_rate = 0.08   # 8% annual growth

step_size = 1.0      # years

end_time = 20        # years

def population_growth(P):
    return growth_rate * P

time = np.arange(
    0,
    end_time + step_size,
    step_size
)

population = np.zeros_like(time)

population[0] = initial_population

# Euler Method
for i in range(len(time) - 1):
    population[i + 1] = (
        population[i]
        + step_size * population_growth(population[i])
    )

# Exact Solution
exact = (
    initial_population
    * np.exp(growth_rate * time)
)

print(
    f"Population after {end_time:.0f} years (Euler): "
    f"{population[-1]:.0f}"
)

print(
    f"Population after {end_time:.0f} years (Exact): "
    f"{exact[-1]:.0f}"
)

print(
    f"Final Absolute Error: "
    f"{abs(population[-1]-exact[-1]):.2f}"
)

plt.plot(
    time,
    population,
    marker='o',
    label='Euler Method'
)

plt.plot(
    time,
    exact,
    label='Exact Solution'
)

plt.xlabel("Time (Years)")
plt.ylabel("Population")

plt.title("Population Growth Model")

plt.legend()
plt.grid(True)

plt.show()