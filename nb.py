import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

iris = load_iris()
X, y = iris.data, iris.target

def fit(X, y):
    classes = np.unique(y)
    mean = [X[y == c].mean(axis=0) for c in classes]
    var = [X[y == c].var(axis=0) for c in classes]
    priors = [np.mean(y == c) for c in classes]
    return mean, var, priors, classes

def predict(X, mean, var, priors, classes):
    def calculate_probabilities(x, mean, var, prior):
        likelihood = np.exp(-0.5 * ((x - mean) ** 2) / var) / np.sqrt(2 * np.pi * var)
        return np.sum(np.log(likelihood))

    predictions = []
    for x in X:
        posteriors = [calculate_probabilities(x, mean[c], var[c], priors[c]) for c in range(len(classes))]
        predictions.append(classes[np.argmax(posteriors)])
    return np.array(predictions)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
mean, var, priors, classes = fit(X_train, y_train)
y_pred = predict(X_test, mean, var, priors, classes)
accuracy = np.mean(y_pred == y_test)
print(f"Accuracy: {accuracy:.4f}")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=iris.target_names))
