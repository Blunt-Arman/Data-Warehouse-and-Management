import pandas as pd
import numpy as np
df = pd.read_csv("Iris.csv")
df['Species'] = df['Species'].map({'Iris-setosa':1, 'Iris-versicolor':2, 'Iris-virginica':3})
X = df.iloc[:, 1:5].values
Y = df['Species'].values
from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(X, Y)
print("Prediction:", model.predict([[5.4, 3.2, 1.2, 0.1]])[0])

