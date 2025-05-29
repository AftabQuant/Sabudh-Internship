import numpy as np
from scipy.special import expit  # Sigmoid function

class RegressionBase:
    def __init__(self, learning_rate=0.01, epochs=1000, regularization=None, lambda_=0.01):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.regularization = regularization
        self.lambda_ = lambda_
        self.beta = None

    def _add_intercept(self, x):
        return np.hstack((np.ones((x.shape[0], 1)), x))

    def _apply_regularization(self, grad):
        if self.regularization == 'l1':
            return grad + self.lambda_ * np.sign(self.beta)
        elif self.regularization == 'l2':
            return grad + self.lambda_ * self.beta
        return grad

    def _compute_cost(self, X, y, y_pred):
        raise NotImplementedError("This method should be implemented by subclasses")

    def _compute_gradient(self, X, y, y_pred):
        raise NotImplementedError("This method should be implemented by subclasses")

    def fit(self, X, y):
        X = self._add_intercept(X)
        self.beta = np.random.randn(X.shape[1], 1)

        for _ in range(self.epochs):
            y_pred = self._predict_raw(X)
            gradient = self._compute_gradient(X, y, y_pred)
            gradient = self._apply_regularization(gradient)
            self.beta -= self.learning_rate * gradient

    def predict(self, X):
        X = self._add_intercept(X)
        return self._predict_raw(X)

class LinearRegression(RegressionBase):
    def _predict_raw(self, X):
        return np.dot(X, self.beta)

    def _compute_cost(self, X, y, y_pred):
        error = y_pred - y
        return np.mean(error ** 2)

    def _compute_gradient(self, X, y, y_pred):
        return (1 / X.shape[0]) * X.T @ (y_pred - y)

class LogisticRegression(RegressionBase):
    def _predict_raw(self, X):
        return expit(np.dot(X, self.beta))

    def _compute_cost(self, X, y, y_pred):
        return -np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))

    def _compute_gradient(self, X, y, y_pred):
        return (1 / X.shape[0]) * X.T @ (y_pred - y)

def generate_dataset(sigma, n, m):
    x = np.random.rand(n, m)
    x = np.hstack((np.ones((n, 1)), x))
    beta = np.random.randn(m + 1, 1)
    noise = np.random.normal(0, sigma, (n, 1))
    y = np.dot(x, beta) + noise
    return x[:, 1:], y, beta

sigma = 1.0
n = 50
m = 2
X, y, beta_true = generate_dataset(sigma, n, m)

# Linear Regression
lr_model = LinearRegression(learning_rate=0.01, epochs=1000, regularization='l2', lambda_=0.1)
lr_model.fit(X, y)
print("Linear Regression Beta:")
print(lr_model.beta)

# Logistic Regression (Simulating binary labels for demonstration)
y_binary = (y > np.mean(y)).astype(int)
log_reg_model = LogisticRegression(learning_rate=0.01, epochs=1000, regularization='l1', lambda_=0.1)
log_reg_model.fit(X, y_binary)
print("\nLogistic Regression Beta:")
print(log_reg_model.beta)
