from scipy.stats import norm

# Given data
mean_diff = -0.05
std_dev_diff = 0.0707

# Calculate the Z-score
z_score = 0.05 / std_dev_diff

# Calculate the probability that Z > z_score
probability = norm.sf(z_score)

print(f"Probability: {probability}")
