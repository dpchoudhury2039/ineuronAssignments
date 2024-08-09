import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Probability in each tail
tail_probability = 0.005

# Calculate the z-value such that P(Z < -z) = 0.005 and P(Z > z) = 0.005
z_value_negative = norm.ppf(tail_probability)
z_value_positive = -z_value_negative  # Symmetry of the standard normal distribution

print(f"The value of z such that P(-z < Z < z) = 0.99 is approximately: ±{z_value_positive:.4f}")

# Visualization
z_values = np.linspace(-4, 4, 1000)
pdf_values = norm.pdf(z_values)

# Plot the standard normal distribution
plt.figure(figsize=(12, 6))
plt.plot(z_values, pdf_values, label='Standard Normal Distribution', color='blue')

# Highlight the central area where P(-z < Z < z) = 0.99
plt.fill_between(z_values, 0, pdf_values, where=(z_values > z_value_negative) & (z_values < z_value_positive), color='green', alpha=0.3, label='P(-z < Z < z) = 0.99')

# Annotate the plot with the z-scores
plt.axvline(x=z_value_negative, color='black', linestyle='--', label=f'-z = {z_value_negative:.4f}')
plt.axvline(x=z_value_positive, color='black', linestyle='--', label=f'z = {z_value_positive:.4f}')
plt.text(z_value_positive + 0.1, 0.02, f'z = {z_value_positive:.4f}', fontsize=12, color='black')
plt.text(z_value_negative - 0.9, 0.02, f'-z = {z_value_negative:.4f}', fontsize=12, color='black')

# Add labels and title
plt.title('Standard Normal Distribution\nHighlighting P(-z < Z < z) = 0.99', fontsize=14)
plt.xlabel('Z', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
