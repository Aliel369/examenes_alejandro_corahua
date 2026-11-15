"""
Ejercicio 02: Procesamiento de números mediante módulos.
"""
import random

def generar_lista_aleatoria(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Error: La cantidad n debe ser un número entero positivo.")
    return [random.randint(1, 100) for _ in range(n)]

def eliminar_duplicados(lista):
    return list(set(lista))

def obtener_ordenamientos(lista):
    ascendente = sorted(lista)
    descendente = sorted(lista, reverse=True)
    return ascendente, descendente

def obtener_mayor_par(lista):
    pares = [num for num in lista if num % 2 == 0]
    if not pares:
        return None
    return max(pares)

def obtener_elemento_por_posicion(lista, posicion):
    if not isinstance(posicion, int):
        raise TypeError("La posición debe ser un número entero.")
    if posicion < 0 or posicion >= len(lista):
        raise IndexError(f"Error: La posición {posicion} está fuera del rango válido (0 a {len(lista)-1}).")
    return lista[posicion]