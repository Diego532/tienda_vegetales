class Producto:
    def __init__(self,id_producto: int, nombre_producto: str,descripcion:str,precio: float,categoria:str, cantidad_en_inventario: int = 0):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria
        self.cantidad_en_inventario = cantidad_en_inventario

    def mostrar_atributos(self):
        print(f"Producto id:{self.id_producto}")
        print(f"Nombre: {self.nombre_producto}")
        print(f"Descripcion: {self.descripcion}")
        print(f"Precio: {self.precio}")
        print(f"Categoria: {self.categoria}")
        print('')

    def cantidad_inventario(self):
        print(f"Cantidad en inventario: {str(self.cantidad_en_inventario)}")

    def aumentar_cantidad_en_inventario(self,cantidad):
        self.cantidad_en_inventario += cantidad

    def restar_cantidad_en_inventario(self,cantidad):
        self.cantidad_en_inventario -= cantidad