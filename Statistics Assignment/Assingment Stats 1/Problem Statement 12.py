import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Given parameters
initial_mean = 0.2508
centered_mean = 0.2500
std_dev = 0.0005

# Specification limits
lsl = 0.2485
usl = 0.2515

# Calculate z-scores for initial condition
z_lower_initial = (lsl - initial_mean) / std_dev
z_upper_initial = (usl - initial_mean) / std_dev

# Calculate proportion within specifications for initial condition
prob_within_spec_initial = norm.cdf(z_upper_initial) - norm.cdf(z_lower_initial)

# Calculate z-scores for centered process
z_lower_centered = (lsl - centered_mean) / std_dev
z_upper_centered = (usl - centered_mean) / std_dev

# Calculate proportion within specifications for centered process
prob_within_spec_centered = norm.cdf(z_upper_centered) - norm.cdf(z_lower_centered)

print(f"Proportion of shafts within specifications (initial mean = 0.2508): {prob_within_spec_initial:.4f}")
print(f"Proportion of shafts within specifications (centered mean = 0.2500): {prob_within_spec_centered:.4f}")

# Visualization
x_values = np.linspace(initial_mean - 5*std_dev, initial_mean + 5*std_dev, 1000)
pdf_values_initial = norm.pdf(x_values, initial_mean, std_dev)
pdf_values_centered = norm.pdf(x_values, centered_mean, std_dev)

plt.figure(figsize=(14, 7))

# Initial process distribution
plt.plot(x_values, pdf_values_initial, label='Initial Distribution (Mean = 0.2508)', color='blue')
plt.fill_between(x_values, 0, pdf_values_initial, where=(x_values > lsl) & (x_values < usl), color='blue', alpha=0.3, label='Within Spec (Initial)')

# Centered process distribution
plt.plot(x_values, pdf_values_centered, label='Centered Distribution (Mean = 0.2500)', color='green')
plt.fill_between(x_values, 0, pdf_values_centered, where=(x_values > lsl) & (x_values < usl), color='green', alpha=0.3, label='Within Spec (Centered)')

# Specification limits
plt.axvline(x=lsl, color='red', linestyle='--', label='Lower Spec Limit (LSL = 0.2485)')
plt.axvline(x=usl, color='red', linestyle='--', label='Upper Spec Limit (USL = 0.2515)')

plt.title('Distribution of Shaft Diameters and Specification Limits')
plt.xlabel('Diameter (inches)')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
