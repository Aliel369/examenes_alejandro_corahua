"""
Ejercicio 03: Funciones y manejo de excepciones
"""

"""Solicitud al usuario de dos valores numéricos."""
def solicitar_dos_numeros():
    while True:
        try:
            print("-" * 40)
            num1 = float(input("Ingrese el primer valor numérico: "))
            num2 = float(input("Ingrese el segundo valor numérico: "))
            return num1, num2
        except ValueError:
            print("Error: Debe ingresar obligatoriamente valores numéricos válidos. Intente nuevamente.")

"""Realización de la división de los dos valores."""
def dividir(a, b):
    while True:
        resultado = None
        try:
            resultado = a / b
        except ZeroDivisionError:
            print("Error: No es posible realizar una división entre cero.")
            print("Por favor, ingrese nuevos valores para reintentar la división:")
            a, b = solicitar_dos_numeros()
            continue
        except TypeError:
            print("Error: Operación entre tipos de datos incompatibles.")
            print("Por favor, ingrese nuevos valores para reintentar la división:")
            a, b = solicitar_dos_numeros()
            continue
        else:
            print("¡¡Operación de división ejecutada correctamente sin excepciones!!")
        finally:
            print("Finalizó el proceso de intento de división.")
        return resultado

"""Realización de la suma de los dos valores."""
def sumar(a, b):
    while True:
        try:
            return a + b
        except TypeError:
            print("Error: Operación entre tipos incompatibles para la suma.")
            print("Por favor, ingrese nuevos valores para reintentar la suma:")
            a, b = solicitar_dos_numeros()

"""Solicitud de la cantidad de elementos a registrar."""
def registrar_elementos():
    while True:
        try:
            print("-" * 40)
            n = int(input("¿Cuántos elementos desea registrar en la lista?: "))
            if n <= 0:
                print("Error: La cantidad de elementos debe ser un número mayor a cero.")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un número válido para la cantidad.")

    lista_datos = []
    for i in range(n):
        while True:
            try:
                elemento = input("Ingrese el elemento {} de {}: ".format(i + 1, n))
                # Intentamos convertir a número si es posible para mayor versatilidad
                if "." in elemento:
                    valor = float(elemento)
                else:
                    try:
                        valor = int(elemento)
                    except ValueError:
                        valor = elemento
                lista_datos.append(valor)
                break
            except Exception as e:
                print("Error al registrar el elemento: {}. Intente de nuevo.".format(e))

    return lista_datos

"""Solicitud del índice."""
def consultar_indice(lista):
    while True:
        try:
            print("-" * 40)
            indice = int(input("Ingrese el índice que desea consultar (0 al {}): ".format(len(lista) - 1)))
            return lista[indice]
        except ValueError:
            print("Error: Debe ingresar un número válido para realizar el índice.")
        except IndexError:
            print("Error: El índice ingresado no existe en la lista. Debe estar entre los valores 0 y {}.".format(len(lista) - 1))


if __name__ == "__main__":
    print("=" * 40)
    print("Sistema de operación y demostración de excepciones")
    print("=" * 40)

    # 1. Solicitar los dos valores numéricos iniciales
    val1, val2 = solicitar_dos_numeros()

    print("=" * 40)
    print("Ejecución de la prueba de la operación suma")
    print("=" * 40)
    resultado_suma = sumar(val1, val2)
    print("El resultado de la suma es: {}".format(resultado_suma))

    print("=" * 40)
    print("Ejecución de la prueba de la operación división")
    print("=" * 40)
    resultado_division = dividir(val1, val2)
    print("El resultado de la división es: {:.2f}".format(resultado_division))

    print("=" * 40)
    print("Registro de los datos en lista")
    print("=" * 40)
    mi_lista = registrar_elementos()
    print("Lista creada exitosamente: {}".format(mi_lista))

    print("=" * 40)
    print("Consulta de los elementos por el índice")
    print("=" * 40)
    elemento_encontrado = consultar_indice(mi_lista)
    print("El elemento ubicado en el índice consultado es: {}".format(elemento_encontrado))

    print("=" * 40)
    print("¡¡Se ha finalizado con éxito!!")
    print("=" * 40)