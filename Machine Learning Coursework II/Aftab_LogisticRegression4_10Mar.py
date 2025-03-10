# When adding L1 and L2 regularization to the Logistic Regression cost function, it essentially penalizes the model for
# having large coefficients, leading to a "shrinking" effect on the learned beta vector (β), which helps prevent overfitting and improves
# the model('s ability to generalize to new data; the choice of the regularization constant (λ) '
# 'directly controls how much the coefficients are shrunk, with a larger λ resulting in more significant '
# shrinkage and potentially causing important features to be dropped in the case of L1 regularization. )

#     Impact on Models Learned :
# 1) L1 Regularization (Lasso):
#   1) Feature Selection: L1 regularization can set some coefficients to zero, effectively performing feature selection. This is
# useful when dealing with a large number of features.
#   2) Model Interpretability: By reducing some coefficients to zero, L1 regularization can improve model interpretability by highlighting the most important features.
#   3) Risk of Underfitting: If λ is too large, L1 regularization can lead to underfitting by setting too many coefficients to zero.
#
# 2) L2 Regularization (Ridge):
#    1) Handling Multicollinearity: L2 regularization reduces the magnitude of all coefficients but does not set them to zero. This helps
# in handling multicollinearity by distributing the effect across correlated features.
#    2) Model Stability: L2 regularization tends to produce more stable models by preventing any single feature
# from dominating the predictions.Risk of Underfitting: Similar to L1, if λ is too large, L2 regularization can lead to underfitting by overly shrinking coefficients.

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# L1 Regularization (Lasso)
logr_l1 = LogisticRegression(penalty='l1', solver='liblinear', max_iter=1000)
logr_l1.fit(X_train, y_train)
print("L1 Regularization Coefficients:", logr_l1.coef_)

# L2 Regularization (Ridge)
logr_l2 = LogisticRegression(penalty='l2', solver='lbfgs', max_iter=1000)
logr_l2.fit(X_train, y_train)
print("L2 Regularization Coefficients:", logr_l2.coef_)

# Impact of lambda
for C in [0.1, 1, 10]:
    logr_l1 = LogisticRegression(penalty='l1', solver='liblinear', C=C, max_iter=1000)
    logr_l1.fit(X_train, y_train)
    print(f"L1 with C={C}: Coefficients - {logr_l1.coef_}")
    logr_l2 = LogisticRegression(penalty='l2', solver='lbfgs', C=C, max_iter=1000)
    logr_l2.fit(X_train, y_train)
    print(f"L2 with C={C}: Coefficients - {logr_l2.coef_}")
