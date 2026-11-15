"""
Pruebas para procesar los números mediante el módulo operaciones.py.
"""
from operaciones import (
    generar_lista_aleatoria,
    eliminar_duplicados,
    obtener_ordenamientos,
    obtener_mayor_par,
    obtener_elemento_por_posicion
)

if __name__ == "__main__":
    print("=== Pruebas de Procesamiento De Números Mediante Módulos ===\n")

    # Pruebas con dos cantidades distintas
    cantidades = [15, 20]

    for idx, n in enumerate(cantidades, 1):
        print(f"--- Ejecución {idx} (Cantidad n = {n}) ---")
        try:
            original = generar_lista_aleatoria(n)
            sin_duplicados = eliminar_duplicados(original)
            asc, desc = obtener_ordenamientos(original)
            mayor_par = obtener_mayor_par(original)

            print(f"Lista original    : {original}")
            print(f"Sin duplicados    : {sin_duplicados}")
            print(f"Orden ascendente  : {asc}")
            print(f"Orden descendente : {desc}")

            if mayor_par is not None:
                print(f"Mayor número par  : {mayor_par}\n")
            else:
                print("Mayor número par  : No existe ningún número par en la lista.\n")

        except (ValueError, TypeError) as e:
            print(f"Error detectado: {e}\n")

    print("--- Pruebas de excepciones y posiciones ---")
    lista_prueba = [10, 25, 42, 13, 8]
    print(f"Lista de prueba estática: {lista_prueba}")

    # 1. Para una posición que es válida
    try:
        pos = 2
        elemento = obtener_elemento_por_posicion(lista_prueba, pos)
        print(f"Posición válida [{pos}] -> Elemento: {elemento}")
    except (IndexError, TypeError) as e:
        print(e)

    # 2. Para una posición fuera del rango
    try:
        pos = 10
        elemento = obtener_elemento_por_posicion(lista_prueba, pos)
        print(f"Posición [{pos}] -> Elemento: {elemento}")
    except (IndexError, TypeError) as e:
        print(f"Capturado correctamente -> {e}")

    # 3. Prueba con una cantidad n inválida
    try:
        print("Intento de generar una lista con n = -5...")
        generar_lista_aleatoria(-5)
    except ValueError as e:
        print(f"Capturado correctamente -> {e}")