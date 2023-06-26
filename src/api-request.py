from urllib.request import urlopen
import json

response = urlopen('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/e20c412e7e1dcc3b089b0594b5a42f30ac15e49b/products.json')
data = json.loads(response.read())
print(data)