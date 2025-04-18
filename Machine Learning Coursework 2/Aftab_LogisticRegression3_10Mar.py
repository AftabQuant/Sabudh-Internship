# Introduction
# Logistic regression is a widely used supervised learning algorithm  for binary classification tasks.
# It relies on the sigmoid function to predict probabilities based on input features. The performance of logistic regression
# depends on several factors, including the sample size n and the learning rate θ. This report investigates how different values
# of n and θ impact the ability of the logistic regression function to learn the coefficients β, which are used to generate the output vector Y.
# Additionally, it includes the derivation of the partial derivative of the cost function with respect to the model parameters.

# Effects on Model Performance:

# 1) Accuracy and Reliability: A larger n tends to reduce the variance of the estimates, leading to more
# reliable models. For logistic regression, a minimum sample size of 500 is often recommended to ensure
# that the estimates are representative of the population parameters.
# 2) Overfitting vs. Underfitting: With small sample sizes, models may overfit or underfit the
# data. Overfitting occurs when the model is too complex and fits the noise in the training data,
# while underfitting happens when the model is too simple to capture the underlying patterns. A sufficient sample size helps mitigate these issues.
# 3) Convergence Speed: A high learning rate can lead to faster convergence but may cause the model to
# overshoot the optimal solution, resulting in oscillations. Conversely, a low learning rate ensures stability but
# may slow down convergence.
# 4) Optimization Stability: If the learning rate is too high, the cost function may increase during training,
# indicating instability. Adjusting the learning rate is essential to ensure that the model converges to a stable minimum


import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import log_loss

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def compute_cost(X, y, beta):
    y_hat = sigmoid(X @ beta)
    return log_loss(y, y_hat)

def gradient_descent(X, y, beta, learning_rate=0.01, epochs=1000):
    m = len(y)
    cost_history = []
    for _ in range(epochs):
        y_hat = sigmoid(X @ beta)
        gradient = (1/m) * X.T @ (y_hat - y)
        beta -= learning_rate * gradient
        cost_history.append(compute_cost(X, y, beta))
    return beta, cost_history

# Example Dataset
np.random.seed(0)
n = 100
X = np.random.rand(n, 2)
y = (X[:, 0] + X[:, 1] > 1).astype(int)
X = np.c_[np.ones(n), X]  # Add intercept term

# Initial Parameters
beta = np.zeros(X.shape[1])
beta, cost_history = gradient_descent(X, y, beta)

# Visualization
plt.plot(cost_history)
plt.title('Cost Function Convergence')
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.grid(True)
plt.show()