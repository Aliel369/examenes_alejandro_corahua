"""
Ejercicio 03: Sistema de registro de pedidos de Rappi.
"""
from datetime import datetime


def registrar_pedido(func):
    def envoltura(*args, **kwargs):
        ahora = datetime.now()  # Obtenemos la fecha y hora
        fecha_hora_str = ahora.strftime("%d/%m/%Y %H:%M:%S")

        print(f"[Log De Sistema] Fecha y hora de ejecución: {fecha_hora_str}")

        resultado = func(*args, **kwargs)

        print("[Log De Sistema] El pedido ha finalizado correctamente.\n")
        return resultado

    return envoltura


@registrar_pedido
def calcular_total(*args):
    for precio in args:  # Validamos que los precios  sean numéricos y mayores que cero
        if not isinstance(precio, (int, float)) or precio <= 0:
            print(f"[Error] El precio detectado es inválido ({precio}). Se cancela el cálculo.")
            return None
    total = sum(args)
    print(f"El cálculo del monto total fue exitoso. Importe: S/. {total:.2f}")
    return total


@registrar_pedido
def procesar_pedido(nombre_cliente, **kwargs):
    print(f"Procesando pedido para el cliente: {nombre_cliente}")
    total = 0.0
    for producto, precio in kwargs.items():
        if not isinstance(precio, (int, float)) or precio <= 0:
            print(
                f"[Error] El producto {producto} tiene un precio inválido ({precio}). No se puede procesar el pedido.")
            return None
        total += precio
    print(f"Importe total para {nombre_cliente}: S/. {total:.2f}")
    return total


if __name__ == "__main__":
    print("=== Prueba de Sistema De Pedidos Rappi ===\n")

    print("--- 1. Ejecución del calcular_total con tres precios ---")
    calcular_total(25.50, 12.00, 8.50)

    print("--- 2. Ejecución del calcular_total con seis precios ---")
    calcular_total(10.0, 15.0, 20.0, 5.5, 12.0, 8.0)

    print("--- 3. Registro del pedido con **kwargs (Para 4 productos válidos) ---")
    procesar_pedido("Benjamín Tennyson", hamburguesa=28.00, papas=10.00, gaseosa=6.50, postre=12.00)

    print("--- 4. Registro del pedido con **kwargs (Con precio negativo) ---")
    procesar_pedido("Deva Cassel", pizza=45.00, cafe=-5.00, agua=4.00)