import pandas as pd
import numpy as np
from math import log
df = pd.read_csv("dataset.csv")
info = -sum(p * log(p, 2) for p in df['class'].value_counts(normalize=True))
print("Total Entropy:", round(info, 4))
for attr in df.drop('class', axis=1):
 info_attr = 0
 for val, prob in df[attr].value_counts(normalize=True).items():
     vc = df[df[attr] == val]['class'].value_counts(normalize=True)
     info_attr += sum(-prob * p * log(p, 2) for p in vc)
     print(f"{attr} → IG: {round(info - info_attr, 4)}")
