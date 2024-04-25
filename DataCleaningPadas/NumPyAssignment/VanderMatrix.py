import numpy as np

def generate_vandermonde(input_vector, n, increasing_order=True):
    return np.vander(input_vector, n, increasing=increasing_order)


input_vector = [1, 2, 3, 4]
n_columns = 4

vandermonde_matrix = generate_vandermonde(input_vector, n_columns, increasing_order=True)

print("Vandermonde Matrix (Ascending Order):")
print(vandermonde_matrix)
