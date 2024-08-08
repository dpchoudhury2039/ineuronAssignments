import math
from scipy.integrate import quad

def pdf(d):
    return 20 * math.exp(-20 * (d - 12.5))

scrap_probability, _ = quad(pdf, 12.6, float('inf'))
print(f"Proportion of Scrapped Parts: {scrap_probability:.4f}")

cdf_11mm = 0
print(f"CDF for 11 mm: {cdf_11mm:.4f}")
