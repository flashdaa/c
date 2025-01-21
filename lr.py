import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_regression(X, y, iterations=200, lr=0.001):
    weights = np.zeros(X.shape[1])
    for _ in range(iterations):
        z = np.dot(X, weights)
        h = sigmoid(z)
        gradient = np.dot(X.T, (h - y)) / y.shape[0]
        weights -= lr * gradient
    return weights

iris = load_iris()
X = iris.data[:, :2]
y = (iris.target != 0).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=9)
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)
weights = logistic_regression(X_train_std, y_train)
y_pred = sigmoid(np.dot(X_test_std, weights)) > 0.5
print(f'Accuracy: {np.mean(y_pred == y_test):.4f}')
plt.scatter(X_train_std[:, 0], X_train_std[:, 1], c=y_train, edgecolor='k')
plt.title('Logistic Regression Decision Boundary')
plt.xlabel('Sepal length (standardized)')
plt.ylabel('Sepal width (standardized)')
plt.show()
