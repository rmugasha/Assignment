import requests, csv
import pandas as pd
import numpy as np
import statistics

response = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
response.columns = ["sepal width","sepal length","petal length","petal width", "flower"]

response.head(10)

