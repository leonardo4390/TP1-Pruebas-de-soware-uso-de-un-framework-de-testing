from producto import Producto

class Tienda:
    def __init__(self):
        self.inventario = []

    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.inventario:
            if producto.nombre == nombre:
                return producto
       # return None
        raise ValueError("Producto no encontrado") # punto 2

    def eliminar_producto(self, nombre):
        for producto in self.inventario:
            if producto.nombre == nombre:
                self.inventario.remove(producto)
                return True
        # return False
        raise ValueError("Producto no encontrado") # punto 2
    
    #punto 3
    def aplicar_descuento(self, nombre, porcentaje):
        producto = self.buscar_producto(nombre)

        nuevo_precio = producto.precio * (1 - porcentaje / 100)

        producto.actualizar_precio(nuevo_precio)