import pandas as pd
df = pd.read_csv("healthcare-dataset-stroke-data.csv")
ages = df['age'].dropna()
print("Mean:", ages.mean())
print("Median:", ages.median())
print("Mode:", ages.mode().tolist())
