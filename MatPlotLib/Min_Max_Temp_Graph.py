import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data for max and min temperatures
months = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # Months (1 to 12)
max_temps = np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
min_temps = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])

# Sine function to fit
def periodic_function(x, amplitude, frequency, phase, offset):
    return amplitude * np.sin(frequency * x + phase) + offset

# Fit the function to the max temperatures
params_max, _ = curve_fit(periodic_function, months, max_temps, p0=[20, 2*np.pi/12, 0, 30])
params_min, _ = curve_fit(periodic_function, months, min_temps, p0=[10, 2*np.pi/12, 0, 20])

# Create a smooth range of x values for plotting
x_smooth = np.linspace(1, 12, 100)

# Get the fitted values for max and min temperatures
max_temps_fit = periodic_function(x_smooth, *params_max)
min_temps_fit = periodic_function(x_smooth, *params_min)

# Plot the data and the fitted functions
plt.figure(figsize=(10, 6))
plt.scatter(months, max_temps, color='red', label='Max Temps (data)')
plt.scatter(months, min_temps, color='blue', label='Min Temps (data)')
plt.plot(x_smooth, max_temps_fit, 'r--', label='Max Temps (fit)')
plt.plot(x_smooth, min_temps_fit, 'b--', label='Min Temps (fit)')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Variation Over the Year')
plt.legend()
plt.show()
