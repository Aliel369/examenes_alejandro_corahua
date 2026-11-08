"""
Ejercicio 04: Registro de participantes con listas
"""

#1 Lista vacía y participantes
participantes = []
participantes.append("Alejandro")
participantes.append("Gabriel")
participantes.append("Jesús")

#2 Agregamos un nuevo participante
participantes.insert(1, "Diego")

#3 Actualizamos el nombre del primero
participantes[0] = "Magdiel"

#4 Eliminamos a uno de la lista
participantes.pop(2)

#5 Lista final y cantidad de participantes
print("Lista final: {}".format(participantes))
print("-------------------")

print("Cantidad de participantes registrados: {}".format(len(participantes)))
print("-------------------")
