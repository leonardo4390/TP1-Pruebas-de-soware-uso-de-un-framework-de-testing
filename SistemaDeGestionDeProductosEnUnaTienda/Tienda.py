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
    # ==========================================================
    # PUNTO 2
    # ==========================================================
        raise ValueError("Producto no encontrado")
    
    # ==========================================================
    # PUNTO 3 - FIXTURE
    # ==========================================================
    def aplicar_descuento(self, nombre, porcentaje):
        producto = self.buscar_producto(nombre)

        nuevo_precio = producto.precio * (1 - porcentaje / 100)

        producto.actualizar_precio(nuevo_precio)
    
    # ==========================================================
    # PUNTO 5 - CALCULAR TOTAL
    # ==========================================================
    def calcular_total_carrito(self, carrito):
        total = 0

        for nombre_producto in carrito:
            producto = self.buscar_producto(nombre_producto)
            total += producto.precio

        return total