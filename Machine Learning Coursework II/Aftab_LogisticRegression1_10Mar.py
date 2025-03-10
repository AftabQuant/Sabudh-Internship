import numpy as np

def generate_data(m, n, theta):
    x = np.hstack((np.ones((n, 1)), np.random.rand(n, m)))
    beta = np.random.randn(m + 1)
    probabilities = 1 / (1 + np.exp(-x @ beta))
    y = (probabilities > 0.5).astype(int)
    noise = np.random.binomial(1, theta, size=n)
    y = np.abs(y - noise)
    return x, y, beta

theta = 0.1
n = 100
m = 5

X, Y, beta = generate_data(m, n, theta)

print("Independent Variables (X):\n", X)
print("\nDependent Variable (Y):\n", Y)
print("\nBeta Coefficients (β):\n", beta)
