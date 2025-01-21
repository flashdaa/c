from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
from collections import Counter
from sklearn.metrics import classification_report, confusion_matrix

iris = load_iris()
data, labels = iris.data, iris.target

train_data, test_data, train_labels, test_labels = train_test_split(
    data, labels, test_size=0.3, random_state=1)

def euclidean_distance(point1, point2):
    return np.linalg.norm(point1 - point2)

def predict(test_point, train_data, train_labels, k):
    distances = [euclidean_distance(test_point, train_point) for train_point in train_data]
    k_indices = np.argsort(distances)[:k]
    k_labels = [train_labels[i] for i in k_indices]
    return Counter(k_labels).most_common(1)[0][0]

def knn(train_data, train_labels, test_data, k):
    return np.array([predict(test_point, train_data, train_labels, k) for test_point in test_data])

k = 3
predicted_labels = knn(train_data, train_labels, test_data, k)
accuracy = np.mean(predicted_labels == test_labels)
print(f"Accuracy: {accuracy:.2f}")
print(confusion_matrix(test_labels, predicted_labels))
print(classification_report(test_labels, predicted_labels))
