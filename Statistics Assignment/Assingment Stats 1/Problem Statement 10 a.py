import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Define the range for Z
z_values = np.linspace(-5, 5, 1000)

# Calculate the PDF for Z
pdf_values = stats.norm.pdf(z_values)

# Plot the PDF
plt.figure(figsize=(14, 7))
plt.plot(z_values, pdf_values, label='Standard Normal Distribution', color='blue')

# Highlight each area

# P(Z > 1.26)
plt.fill_between(z_values, 0, pdf_values, where=(z_values > 1.26), color='red', alpha=0.3, label='P(Z > 1.26)')

# P(Z < -0.86)
plt.fill_between(z_values, 0, pdf_values, where=(z_values < -0.86), color='green', alpha=0.3, label='P(Z < -0.86)')

# P(Z > -1.37)
plt.fill_between(z_values, 0, pdf_values, where=(z_values > -1.37), color='purple', alpha=0.3, label='P(Z > -1.37)')

# P(-1.25 < Z < 0.37)
plt.fill_between(z_values, 0, pdf_values, where=(z_values > -1.25) & (z_values < 0.37), color='orange', alpha=0.3, label='P(-1.25 < Z < 0.37)')

# P(Z <= -4.6)
plt.fill_between(z_values, 0, pdf_values, where=(z_values <= -4.6), color='cyan', alpha=0.3, label='P(Z <= -4.6)')

# Add labels and legend
plt.title('Standard Normal Distribution with Highlighted Areas')
plt.xlabel('Z')
plt.ylabel('Probability Density')
plt.legend()

plt.grid(True)
plt.show()
