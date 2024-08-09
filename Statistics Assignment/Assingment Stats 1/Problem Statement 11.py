import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Given parameters
mean = 10  # Mean of the distribution
std_dev = 2  # Standard deviation (square root of variance)

# 1. Probability that current exceeds 13 mA
z_score_13 = (13 - mean) / std_dev
prob_exceed_13 = 1 - norm.cdf(z_score_13)

print(f"Probability that the current exceeds 13 mA: {prob_exceed_13:.4f}")

# 2. Probability that current is between 9 and 11 mA
z_score_9 = (9 - mean) / std_dev
z_score_11 = (11 - mean) / std_dev

prob_between_9_11 = norm.cdf(z_score_11) - norm.cdf(z_score_9)
print(f"Probability that the current is between 9 and 11 mA: {prob_between_9_11:.4f}")

# 3. Current measurement with probability of 0.98
z_value_98 = norm.ppf(0.98)
current_98 = mean + z_value_98 * std_dev

print(f"The current measurement with a probability of 0.98: {current_98:.4f} mA")

# Visualization
z_values = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
pdf_values = norm.pdf(z_values, mean, std_dev)

plt.figure(figsize=(12, 6))
plt.plot(z_values, pdf_values, label='Normal Distribution', color='blue')

# Highlight area for P(X > 13)
plt.fill_between(z_values, 0, pdf_values, where=(z_values > 13), color='red', alpha=0.3, label='P(X > 13 mA)')

# Highlight area for P(9 < X < 11)
plt.fill_between(z_values, 0, pdf_values, where=(z_values > 9) & (z_values < 11), color='green', alpha=0.3, label='P(9 < X < 11 mA)')

# Annotate the plot for 98% probability
plt.axvline(x=current_98, color='purple', linestyle='--', label=f'0.98 Probability (X = {current_98:.2f} mA)')
plt.text(current_98 + 0.1, 0.02, f'{current_98:.2f} mA', fontsize=12, color='purple')

plt.title('Normal Distribution of Current Measurements', fontsize=14)
plt.xlabel('Current (mA)', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
