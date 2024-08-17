import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("Dosya konumu/IMBD.csv")

silinecekColumns=["genre","rating","description","stars","votes"]
print(df.drop(silinecekColumns,axis=1).head(10))






