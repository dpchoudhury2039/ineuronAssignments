import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Desired probability for the upper tail
p = 0.05

# Calculate z such that P(Z > z) = 0.05
z_value = norm.ppf(1 - p)

print(f"The value of z such that P(Z > z) = 0.05 is approximately: {z_value:.4f}")

# Create a range of z-values
z_values = np.linspace(-3, 3, 1000)
pdf_values = norm.pdf(z_values)

# Plot the standard normal distribution
plt.figure(figsize=(12, 6))
plt.plot(z_values, pdf_values, label='Standard Normal Distribution', color='blue')

# Highlight the area where P(Z > z) = 0.05
plt.fill_between(z_values, 0, pdf_values, where=(z_values > z_value), color='red', alpha=0.3, label='P(Z > z) = 0.05')

# Annotate the plot with the z-score
plt.axvline(x=z_value, color='black', linestyle='--', label=f'z = {z_value:.4f}')
plt.text(z_value + 0.1, 0.02, f'z = {z_value:.4f}', fontsize=12, color='black')

# Add labels and title
plt.title('Standard Normal Distribution\nHighlighting P(Z > z) = 0.05', fontsize=14)
plt.xlabel('Z', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
