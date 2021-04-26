import requests

response = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
response.text
