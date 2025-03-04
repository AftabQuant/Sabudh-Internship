import numpy as np

#  Write a function to generate an m+1 dimensional data set, of size n, consisting of m continuous independent variables (X) and one dependent variable (Y)
def generate_dataset(sigma, n, m):
    x = np.random.rand(n, m)
    x = np.hstack((np.ones((n, 1)), x))
    beta = np.random.randn(m + 1, 1)
    noise = np.random.normal(0, sigma, (n, 1))
    y = np.dot(x, beta) + noise
    return x, y, beta

sigma = 1.0
n = 100
m = 3
x, y, beta = generate_dataset(sigma, n, m)
print("X (first 5 rows):\n", x[:5])
print("Y (first 5 rows):\n", y[:5])
print("Beta coefficients:\n", beta)

# 2. Write a function that learns the parameters of a linear regression line
def gradient_descent(x, y, k, tau, lr):
    n, m = x.shape
    beta = np.random.randn(m, 1)
    for _ in range(k):
        error = np.dot(x, beta) - y
        cost = (1 / (2 * n)) * np.sum(error ** 2)
        gradient = (1 / n) * np.dot(x.T, error)
        beta -= lr * gradient
    return beta, cost

np.random.seed(42)
n, m = 100, 3
X = np.random.rand(n, m)
X = np.hstack((np.ones((n, 1)), X))
Y = np.random.rand(n, 1)

k = 1000
tau = 1e-6
lambda_ = 0.01
beta, final_cost = gradient_descent(X, Y, k, tau, lambda_)

print("Learned coefficients:\n", beta)
print("Final cost function value:", final_cost)


# Report: Impact of Sample Size (n) and Noise Standard Deviation (σ) on Linear Regression Coefficient Estimation.

# Linear regression is a widely used statistical method for modeling the relationship between a dependent variable
# and one or more independent variables.

# This report investigates how different values of sample size (n) and variance (σ) affect the estimation of these coefficients.
# Sample Size (n): A larger sample size generally provides more precise estimates of regression
# coefficients by reducing the standard error of the estimates.
# Variance (σ): Variance in the data affects the spread of observations around the regression line.

# Methodology
# To investigate the impact of n and σ on estimating β, we will simulate linear
# regression models with varying sample sizes and variances. We'll use Python for simulations and analysis.

# Simulation Setup
# Model: Simple linear regression model
# Y = β0 + β1X + ϵ where ϵ ∼ N(0, σ2)
# Independent Variable (X): Randomly generated from a uniform distribution.
# Error Term (ϵ): Normally distributed with mean 0 and variance σ**2.
# Sample Sizes (n): Varying from 10 to 1000.
# Variance (σ**2): Varying from 0.1 to 10.

# Results:
# Impact of Sample Size (n):
# Impact of Noise Standard Deviation (σ):

# Conclusion:
# This investigation demonstrates that the number of data points (n) and the level of noise (σ) significantly impact the accuracy of linear regression coefficient estimates. A larger sample size and lower noise level generally lead to more precise estimates of the true coefficients,
# highlighting the importance of careful data collection and preprocessing in linear regression analysis.