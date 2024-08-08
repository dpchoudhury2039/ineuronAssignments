import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

# Parameters for Gaurav
n_g = 8
p_g = 0.75

# Parameters for Barakha
n_b = 12
p_b = 0.45

# Number of correct solutions
x = np.arange(0, 13)

# Probability distributions
prob_g = binom.pmf(x, n_g, p_g)
prob_b = binom.pmf(x, n_b, p_b)

# Plotting the distribution
plt.figure(figsize=(12, 6))
plt.plot(x, prob_g, label="Gaurav (n=8, p=0.75)", marker='o')
plt.plot(x, prob_b, label="Barakha (n=12, p=0.45)", marker='s')

plt.xticks(np.arange(0, 13, 1))
plt.xlabel("Number of Correct Solutions")
plt.ylabel("Probability")
plt.title("Probability Distribution of Correct Solutions for Gaurav and Barakha")
plt.legend()
plt.grid(True)
plt.show()
