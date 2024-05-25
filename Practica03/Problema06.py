class Producto:
    def __init__(self, nombre, precio, marca, año):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.año = año

    def __str__(self):
        return f"{self.nombre} - {self.marca} - {self.año} - ${self.precio}"


class Catalogo:
    Productos=[]
    def __init__(self,Productos=[]):
        self.productos= Productos

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        for producto in productos_filtrados:
            print(producto)



catalogo = Catalogo()

producto1 = Producto("Llantas", 100, "Goodyear", 2020)
producto2 = Producto("Filtros de Aceite", 20, "Bosch", 2021)
producto3 = Producto("Pastillas de Freno", 50, "ACDelco", 2019)

catalogo.agregar_producto(producto1)
catalogo.agregar_producto(producto2)
catalogo.agregar_producto(producto3)

print("Todos los productos:")
catalogo.mostrar_productos()

print("\nProductos del año 2020:")
catalogo.filtrar_por_año(2020)