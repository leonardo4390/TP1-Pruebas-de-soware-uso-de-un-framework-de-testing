from producto import Producto

def test_crear_producto():
    producto = Producto("Remera", 10000, "Indumentaria")

    assert producto.nombre == "Remera"
    assert producto.precio == 10000
    assert producto.categoria == "Indumentaria"