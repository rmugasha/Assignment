import requests, csv
import pandas as pd

response1 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(response1.head())