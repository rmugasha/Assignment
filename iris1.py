import requests, csv
import pandas as pd
import numpy as np
import statistics
import seaborn as sns

iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
iris.columns = ["sepal width","sepal length","petal length","petal width", "flower"]
iris = iris.dropna()
iris = pd.DataFrame(data = iris, columns = ["sepal width","sepal length","petal length","petal width"])
iris.head(10)

iris.describe()

sns.scatterplot(data=iris, x = "petal length" , y= "petal width")

sns.pairplot(iris)

