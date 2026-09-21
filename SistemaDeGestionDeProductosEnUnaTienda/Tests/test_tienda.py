import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from unittest.mock import Mock # punto 3
from tienda import Tienda
from producto import Producto

"""
def test_agregar_producto():
    tienda = Tienda()
    producto = Producto("Remera", 10000, "Indumentaria")

    tienda.agregar_producto(producto)

    assert producto in tienda.inventario

def test_buscar_producto_existente():
    tienda = Tienda()
    producto = Producto("Remera", 10000, "Indumentaria")

    tienda.agregar_producto(producto)

    resultado = tienda.buscar_producto("Remera")

    assert resultado == producto

def test_buscar_producto_no_existente():
    tienda = Tienda()

    # resultado = tienda.buscar_producto("Zapatilla")

    # assert resultado is None
    # punto 2
    with pytest.raises(ValueError):
        tienda.eliminar_producto("Zapatilla")
    

def test_eliminar_producto():
    tienda = Tienda()
    producto = Producto("Remera", 10000, "Indumentaria")

    tienda.agregar_producto(producto)

    resultado = tienda.eliminar_producto("Remera")

    assert resultado is True
    assert producto not in tienda.inventario

# punto 2
def test_eliminar_producto_inexistente():
    tienda = Tienda()

    with pytest.raises(ValueError):
        tienda.eliminar_producto("Zapatilla")
"""
# ==========================================================
# PUNTO 4 - FIXTURE
# ==========================================================

@pytest.fixture
def tienda_con_productos():
    tienda = Tienda()

    tienda.agregar_producto(
        Producto("Remera", 10000, "Indumentaria")
    )

    tienda.agregar_producto(
        Producto("Pantalon", 20000, "Indumentaria")
    )

    tienda.agregar_producto(
        Producto("Zapatillas", 30000, "Calzado")
    )

    return tienda


# ==========================================================
# PUNTO 1 - AGREGAR PRODUCTO
# ==========================================================

def test_agregar_producto(tienda_con_productos):
    nuevo_producto = Producto(
        "Campera",
        40000,
        "Indumentaria"
    )

    tienda_con_productos.agregar_producto(nuevo_producto)

    assert nuevo_producto in tienda_con_productos.inventario


# ==========================================================
# PUNTO 1 - BUSCAR PRODUCTO
# ==========================================================

def test_buscar_producto_existente(tienda_con_productos):
    resultado = tienda_con_productos.buscar_producto("Remera")

    assert resultado.nombre == "Remera"
    assert resultado.precio == 10000


# ==========================================================
# PUNTO 2 - BUSCAR PRODUCTO INEXISTENTE
# ==========================================================

def test_buscar_producto_no_existente():
    tienda = Tienda()

    with pytest.raises(ValueError):
        tienda.buscar_producto("Zapatilla")


# ==========================================================
# PUNTO 1 - ELIMINAR PRODUCTO
# ==========================================================

def test_eliminar_producto():
    tienda = Tienda()

    producto = Producto(
        "Remera",
        10000,
        "Indumentaria"
    )

    tienda.agregar_producto(producto)

    resultado = tienda.eliminar_producto("Remera")

    assert resultado is True
    assert producto not in tienda.inventario


# ==========================================================
# PUNTO 2 - ELIMINAR PRODUCTO INEXISTENTE
# ==========================================================

def test_eliminar_producto_inexistente():
    tienda = Tienda()

    with pytest.raises(ValueError):
        tienda.eliminar_producto("Zapatilla")


# ==========================================================
# PUNTO 3 - APLICAR DESCUENTO CON MOCK
# ==========================================================

def test_aplicar_descuento():
    tienda = Tienda()

    producto_mock = Mock()

    producto_mock.nombre = "Remera"
    producto_mock.precio = 10000

    tienda.inventario.append(producto_mock)

    tienda.aplicar_descuento("Remera", 20)

    producto_mock.actualizar_precio.assert_called_once_with(8000)
    
    
    
