from math import comb, sqrt

n = 6
p = 0.30
k = 2
q = 1 - p

probability_2_faulty = comb(n, k) * (p ** k) * (q ** (n - k))
print("Probability of 2 faulty LEDs", probability_2_faulty)

mean = n * p
print("Average value of the process", mean)

standard_deviation = sqrt(n * p * q)
print("Standard Deviation", standard_deviation)
