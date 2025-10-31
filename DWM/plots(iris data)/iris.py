import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Iris.csv")
# Histogram
df['PetalWidthCm'].plot(kind='hist', bins=20, edgecolor='black', title="Histogram of Petal Width")
plt.show()
# Scatter
df.plot(kind='scatter', x='SepalLengthCm', y='PetalLengthCm', title="Sepal vs Petal Length")
plt.show()
# Pie
df['Species'].value_counts().plot(kind='pie', autopct='%1.1f%%', title="Species Distribution")
plt.show()
# Boxplot
df['PetalLengthCm'].plot(kind='box', title="Boxplot of Petal Length")
plt.show()
# Line
df.plot(x='SepalLengthCm', y='PetalLengthCm', marker='o', title="Line: Sepal vs Petal Length")
plt.show()
# Bar
df.groupby('Species')['PetalLengthCm'].mean().plot(kind='bar', title="Avg Petal Length by Species")
plt.show()
