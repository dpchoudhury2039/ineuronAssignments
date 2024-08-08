import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Given data
lambda_rate = 4.8  # Average rate of customers in 4 minutes

# Calculate probabilities
p_5_customers = poisson.pmf(5, lambda_rate)
p_not_more_than_3 = sum(poisson.pmf(k, lambda_rate) for k in range(0, 4))
p_more_than_3 = 1 - p_not_more_than_3

# Display results
print(f"Probability of exactly 5 customers: {p_5_customers:.5f}")
print(f"Probability of not more than 3 customers: {p_not_more_than_3:.5f}")
print(f"Probability of more than 3 customers: {p_more_than_3:.5f}")

# Pictorial representation
x_values = np.arange(0, 15)
probabilities = poisson.pmf(x_values, lambda_rate)

plt.figure(figsize=(10, 6))
plt.bar(x_values, probabilities, color='skyblue')
plt.axvline(x=5, color='red', linestyle='--', label='5 Customers')
plt.axvline(x=3, color='green', linestyle='--', label='3 Customers')
plt.xticks(x_values)
plt.xlabel('Number of Customers')
plt.ylabel('Probability')
plt.title('Poisson Distribution of Customer Arrivals')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
