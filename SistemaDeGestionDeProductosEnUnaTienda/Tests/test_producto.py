import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from producto import Producto

def test_crear_producto():
    producto = Producto("Remera", 10000, "Indumentaria")

    assert producto.nombre == "Remera"
    assert producto.precio == 10000
    assert producto.categoria == "Indumentaria"

# punto 2
def test_actualizar_precio_negativo():
    producto = Producto("Remera", 10000, "Indumentaria")

    with pytest.raises(ValueError):
        producto.actualizar_precio(-5000)