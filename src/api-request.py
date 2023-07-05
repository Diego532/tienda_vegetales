from urllib.request import urlopen
from gestion_productos.producto import Producto
import json

response = urlopen('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/e20c412e7e1dcc3b089b0594b5a42f30ac15e49b/products.json')
data = json.loads(response.read())

categorias = set()
lista_productos = []
for producto in data:
    producto_actual = Producto('1',producto.get('name'),producto.get('description'),producto.get('price'),producto.get('category'))
    producto_actual.mostrar_atributos()
    print(' ')
    lista_productos.append(producto_actual)
    categorias.add(producto.get('category'))

print(categorias)
print(lista_productos)


