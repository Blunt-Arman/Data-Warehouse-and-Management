import pandas as pd
import numpy as np
df = pd.read_csv("salary.csv")
X, Y = df.iloc[:, 0].values, df.iloc[:, 1].values
m = ((X - X.mean())*(Y - Y.mean())).sum() / ((X - X.mean())**2).sum()
b = Y.mean() - m*X.mean()
Exp = int(input("Enter Experience: "))
print("Predicted Salary:", m*Exp + b)
