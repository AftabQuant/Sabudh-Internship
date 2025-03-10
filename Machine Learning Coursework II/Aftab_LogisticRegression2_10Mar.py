import numpy as np

def sigmoid_function(z):
    return 1 / (1 + np.exp(-z))

def cost_function(x, y, beta):
    m = len(y)
    predictions = sigmoid_function(x @ beta)
    loss = -np.mean(y * np.log(predictions) + (1 - y) * np.log(1 - predictions))
    return loss

def logistic_regression(x, y, K, tau, lr):
    beta = np.random.randn(x.shape[1])
    pc = cost_function(x, y, beta)
    for _ in range(K):
        predict = sigmoid_function(x @ beta)
        gradient = (x.T @ (predict - y)) / len(y)
        beta -= lr * gradient
        cc = cost_function(x, y, beta)
        if abs(pc - cc) < tau:
            break
        pc = cc
    return beta, cc

X = np.c_[np.ones(50), np.random.rand(50, 5)]
Y = (np.random.rand(50) > 0.5).astype(int)
k = 100
tau = 1e-6
lr = 0.01
beta, final_cost = logistic_regression(X, Y, k, tau, lr)
print("Beta Coefficients:\n", beta)
print("\nFinal Cost Function Value:\n", final_cost)
