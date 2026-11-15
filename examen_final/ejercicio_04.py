"""
Ejercicio 04: Control de inventario mediante diccionarios.
"""

# Realizamos el diccionario inicial con 4 productos
inventario = {
    "P001": {"nombre": "Laptop Gamer", "precio": 3500.00, "stock": 10},
    "P002": {"nombre": "Mouse Inalámbrico", "precio": 75.50, "stock": 25},
    "P003": {"nombre": "Teclado Mecánico", "precio": 220.00, "stock": 15},
    "P004": {"nombre": "Monitor 25 pulgadas", "precio": 850.00, "stock": 8}
}


def mostrar_inventario(dic_inventario):
    print("--- Estado actual del inventario ---")
    for codigo, info in dic_inventario.items():
        print(
            f"Código: {codigo} | Producto: {info['nombre']} | Precio: S/. {info['precio']:.2f} | Stock: {info['stock']} unidades")
    print("-" * 40)


def realizar_compra(dic_inventario, codigo_producto, cantidad_solicitada):
    print(f"\nRealizando compra de {cantidad_solicitada} unidad(es) del código {codigo_producto}...")

    if codigo_producto not in dic_inventario: # Validación de la existencia de la clave del producto
        print(f"[Error] El producto con código {codigo_producto} no existe en el inventario.")
        return False

    producto = dic_inventario[codigo_producto]

    if cantidad_solicitada > producto['stock']: # Validación de disponibilidad de stock
        print(
            f"[Error] Stock insuficiente para {producto['nombre']}. Stock disponible: {producto['stock']}, Solicitado: {cantidad_solicitada}.")
        return False

    if cantidad_solicitada <= 0:
        print("[Error] La cantidad solicitada debe ser mayor a cero.")
        return False

    importe_compra = producto['precio'] * cantidad_solicitada # Calculo del importe y actualización de existencias
    producto['stock'] -= cantidad_solicitada

    print(
        f"¡La compra fue exitosa! Producto: {producto['nombre']} | Cantidad: {cantidad_solicitada} | Importe total: S/. {importe_compra:.2f}")
    return True


def calcular_valor_inventario(dic_inventario):
    valor_total = sum(item['precio'] * item['stock'] for item in dic_inventario.values())
    return valor_total


if __name__ == "__main__":
    print("=== Pruebas de Control De Inventario ===\n")

    # 1. Mostramos el inventario inicial
    mostrar_inventario(inventario)

    # 2. Por la compra válida
    realizar_compra(inventario, "P003", 2)

    # 3. Por la compra de un producto inexistente
    realizar_compra(inventario, "P999", 1)

    # 4. Por la compra con cantidad superior al stock
    realizar_compra(inventario, "P001", 50)

    print("\n")
    # 5. Mostramos el inventario actualizado y su valor total
    mostrar_inventario(inventario)
    valor_total_inventario = calcular_valor_inventario(inventario)
    print(f"Valor Total Del Inventario: S/. {valor_total_inventario:.2f}")