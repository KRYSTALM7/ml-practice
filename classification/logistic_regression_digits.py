"""
Logistic Regression on Digits Dataset (image classification)
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

digits = load_digits()
print("Image data shape:", digits.data.shape)
print("Label data shape:", digits.target.shape)

x_train, x_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.25, random_state=0)

plt.imshow(np.reshape(x_train[1], (8, 8)), cmap='gray')
plt.title("Sample Training Image")
plt.show()

model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

predictions = model.predict(x_test)
print("Accuracy:", model.score(x_test, y_test))
print("Confusion Matrix:\n", metrics.confusion_matrix(y_test, predictions))