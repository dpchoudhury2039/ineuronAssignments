import scipy.stats as stats

# Data
group1 = [51, 45, 33, 45, 67]
group2 = [23, 43, 23, 43, 45]
group3 = [56, 76, 74, 87, 56]

# Perform One-Way ANOVA
f_stat, p_value = stats.f_oneway(group1, group2, group3)

print(f"F-Statistic: {f_stat}")
print(f"P-Value: {p_value}")
