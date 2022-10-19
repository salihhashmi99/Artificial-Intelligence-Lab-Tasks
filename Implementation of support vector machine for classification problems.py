import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("D:\Salih\iris_data.csv")
print("Original Data:\n",dataset.head())#Original Data
X = dataset.iloc[:, :-1].values #Setting input features equal to X
y = dataset.iloc[:,-1].values #Setting Output features equal to y
print(X.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, shuffle = True)
print("Training Set: ",X_train.shape)
print("Test Set: ", X_test.shape )

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print("Confusion Matrix:\n",confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(y_test, y_pred)*100,"%")
