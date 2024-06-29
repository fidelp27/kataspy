'''
Sistema de Gestión de Inventario
Enunciado:
Crea un sistema de gestión de inventario con las siguientes clases y características:

Clase Producto: con atributos nombre, precio, y cantidad. Métodos:

actualizar_precio(nuevo_precio): actualiza el precio del producto.
actualizar_cantidad(nueva_cantidad): actualiza la cantidad del producto.
__str__(): devuelve una cadena con la información del producto.


Clase Inventario: con un atributo productos (lista de productos). Métodos:

agregar_producto(producto): agrega un producto al inventario.
eliminar_producto(producto): elimina un producto del inventario.
actualizar_producto(producto, nuevo_precio, nueva_cantidad): actualiza el precio y la cantidad de un producto.
mostrar_inventario(): imprime todos los productos en el inventario.
'''
class Producto:
  def __init__(self, nombre, precio, cantidad):
    self.nombre = nombre
    self.precio = precio
    self.cantidad = cantidad
  def nuevo_precio(self, nuevo_precio):
    self.precio = nuevo_precio
  def nueva_cantidad(self, nueva_cantidad):
    self.cantidad = nueva_cantidad
  def __str__(self):
    return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad:{self.cantidad}"
  def __repr__(self):
    return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad:{self.cantidad}"

class Inventario:
  def __init__(self):
    self.lista_productos = []
  def agregar_producto(self, producto):
    self.lista_productos.append(producto)
  def eliminar_producto(self, producto):
    self.lista_productos.remove(producto)
  def actualizar_producto(self, producto, nuevo_precio, nueva_cantidad):
    producto.nuevo_precio(nuevo_precio)
    producto.nueva_cantidad(nueva_cantidad)
  def mostrar_inventario(self):
    return [producto for producto in self.lista_productos if producto.cantidad > 0]

producto1 = Producto("Producto 1", 10, 5)
producto2 = Producto("Producto 2", 20, 10)
inventario1 = Inventario()
inventario1.agregar_producto(producto1)
inventario1.agregar_producto(producto2)
print(inventario1.mostrar_inventario())
inventario1.actualizar_producto(producto1, 15, 3)
print(inventario1.mostrar_inventario())