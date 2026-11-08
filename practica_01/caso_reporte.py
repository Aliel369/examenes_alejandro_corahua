"""
Ejercicio 2: Calificaciones
"""

#1 Calificaciones y pesos
matematicas = 17.0                   #Uso datos tipo float porque en la realidad las notas salen con decimales
ciencia = 14.0
historia = 15.0

peso_matematicas = 0.40
peso_ciencia = 0.30
peso_historia = 0.30

#2 Nota final
nota_final = (matematicas * peso_matematicas) + (ciencia * peso_ciencia) + (historia * peso_historia)
print("La nota final del alumno es de: {}".format(f"{nota_final:.1f}"))  #Se hace uso de un decimal
print("-------------------")

#3 Evaluación de aprobación
nota_final >= 13.0          #Este es el dato booleano
print("¿Aprobado?: {}".format(nota_final >= 13.0))
print("-------------------")

#4 La cadena de resumen
if nota_final >= 13.0:
    print("El estudiante obtuvo una nota final de {} y su estado final es: Aprobado".format(f"{nota_final:.1f}"))
print("-------------------")

if nota_final < 13.0:
    print("El estudiante obtuvo una nota final de {} y su estado final es: Desaprobado".format(f"{nota_final:.1f}"))
