#importing pandas
import pandas as pd
#importing numpy
import numpy as np
#importing matplotlib
import matplotlib.pyplot as plt
#importing seaborn 
import seaborn as sb
#reading csv file
df=pd.read_csv("country_vaccinations.csv")
print(df.head(10))
print(df.isnull().sum())
missing_values=["N/A","n/a","na","NA",np.nan]
df=pd.read_csv("country_vaccinations.csv",na_values=missing_values)
print(df.isnull().sum())
#df.dropna()
# Visualize missing values using a heatmap (optimize by using a subset of data)
print(df.tail())
df1=sb.load_dataset("country_vaccinations.csv")
sb.heatmap(df1.isnull(),yticklabels=False,annot=True)
plt.show()