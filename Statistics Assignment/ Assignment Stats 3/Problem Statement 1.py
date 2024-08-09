from scipy.stats import norm

# Given data
population_mean = 100
population_std = 15
sample_mean = 108
sample_size = 36

# Calculate the z-score
z_score = (sample_mean - population_mean) / (population_std / (sample_size ** 0.5))

# Calculate the p-value for a two-tailed test
p_value = 2 * norm.sf(z_score)

print(f"Z-score: {z_score}")
print(f"P-value: {p_value}")
