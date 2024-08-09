from scipy.stats import norm

# Given data
mean = 1026
std_dev = 209
score = 1100

# Calculate the z-score
z_score = (score - mean) / std_dev

# Calculate the percentile rank
percentile_rank = norm.cdf(z_score)

print(f"Z-score: {z_score}")
print(f"Percentile Rank: {percentile_rank * 100:.2f}%")
