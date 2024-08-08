import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Lambda values for different word counts
lambda_values = {
    "455 Words": 0.5908,
    "1000 Words": 1.2987,
    "255 Words": 0.3312
}

# Word count scenarios
x = np.arange(0, 10)  # Possible number of errors

# Plotting
plt.figure(figsize=(12, 6))

for scenario, lam in lambda_values.items():
    probabilities = poisson.pmf(x, lam)
    plt.plot(x, probabilities, marker='o', linestyle='-', label=f'{scenario} (λ={lam:.4f})')

plt.xticks(x)
plt.xlabel('Number of Errors')
plt.ylabel('Probability')
plt.title('Poisson Distribution for Different Word Counts')
plt.legend()
plt.grid(True)
plt.show()
