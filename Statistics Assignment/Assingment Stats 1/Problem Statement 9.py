import numpy as np
import matplotlib.pyplot as plt

# Define the PDF function
def pdf(d):
    return 20 * np.exp(-20 * (d - 12.5))

# Define the range for d
d_values = np.linspace(12.5, 12.8, 400)

# Calculate PDF values
pdf_values = pdf(d_values)

# Calculate CDF values
cdf_values = 1 - np.exp(-20 * (d_values - 12.5))

# Plot the PDF and CDF
plt.figure(figsize=(12, 6))

# Plot PDF
plt.subplot(1, 2, 1)
plt.plot(d_values, pdf_values, label='PDF', color='b')
plt.fill_between(d_values, 0, pdf_values, where=(d_values > 12.6), color='r', alpha=0.3, label='Scrap Area')
plt.title('Probability Density Function (PDF)')
plt.xlabel('Diameter (mm)')
plt.ylabel('Probability Density')
plt.legend()

# Plot CDF
plt.subplot(1, 2, 2)
plt.plot(d_values, cdf_values, label='CDF', color='g')
plt.axvline(x=12.6, color='r', linestyle='--', label='Scrap Threshold')
plt.title('Cumulative Distribution Function (CDF)')
plt.xlabel('Diameter (mm)')
plt.ylabel('Cumulative Probability')
plt.legend()

plt.tight_layout()
plt.show()
