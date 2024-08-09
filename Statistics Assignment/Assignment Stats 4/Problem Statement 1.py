import scipy.stats as stats
import numpy as np

# Observed frequencies
observed = np.array([[60, 40], [54, 44], [46, 53], [41, 57]])

# Perform Chi-Square Test
chi2_stat, p_value, dof, expected = stats.chi2_contingency(observed)

print(f"Chi-Square Statistic: {chi2_stat}")
print(f"P-Value: {p_value}")
print(f"Degrees of Freedom: {dof}")
print(f"Expected Frequencies:\n{expected}")

# Decision based on p-value
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: Gender and education level are dependent.")
else:
    print("Fail to reject the null hypothesis: Gender and education level are independent.")
