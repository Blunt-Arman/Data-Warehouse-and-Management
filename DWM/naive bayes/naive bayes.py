import pandas as pd
df = pd.read_csv("dataset.csv")
age = input("Age: ")
income = input("Income: ")
student = input("Student (yes/no): ")
credit = input("Credit rating: ")
subset = df[(df['age']==age)&(df['income']==income)&(df['student']==student)&(df['credit_rating']==credit)]
pred = subset['class'].mode()[0] if not subset.empty else df['class'].mode()[0]
print("Predicted class:", pred.upper())
