import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("WEATHER_tokyo_data.csv")


print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

df.hist(figsize=(10,8))
plt.show()

df.plot(kind='box', subplots=True, layout=(2,2), figsize=(10,8))
plt.show()