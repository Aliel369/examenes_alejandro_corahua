"""
Ejercicio 1: Tipo de datos (Salario)
"""

#1 Asignar en variables los datos...
nombre = "Yu"
salario = 2500.0
edad = "24"
compania = "Atlus"   #No puedo escribir compania con tilde y enie

print("Nombre del trabajador: {}".format(nombre))
print("El tipo de mi variable de 'nombre' es: {}".format(type(nombre)))
print("-------------------")

print("Salario del trabajador: {}".format(salario))
print("El tipo de mi variable de 'salario' es {}".format(type(salario)))
print("-------------------")

print("Edad del trabajador: {}".format(edad))
print("El tipo de mi variable para 'edad' es {}".format(type(edad)))
print("-------------------")

print("Compañía del trabajador: {}".format(compania))
print("El tipo de mi variable para 'compañía' es {}".format(type(compania)))
print("-------------------")

#2 Conversión de string a int...
edad_int = int(edad)     #Lo convierto a entero para operar

#3 Identificar si la edad...
if edad_int > 30:
    print("Usted tiene un bono del 10% en el mes de diciembre")    #Cambie el "de" por "del"
print("-------------------")

if edad_int <= 30:
    print("Usted tiene un bono del 5% en el mes de diciembre")
print("-------------------")

#4 Mostrar el bono final...
if edad_int > 30:
    bono_final = (salario ** 2) + (salario * 0.10)
    print("El bono final es de: S/ {}".format(f"{bono_final:.2f}"))
print("-------------------")

if edad_int <= 30:
    bono_final = (salario ** 2) + (salario * 0.05)
    print("El bono final es de: S/ {}".format(f"{bono_final:.2f}"))
print("-------------------")
print("-------------------")
#PDST: El bono es un monto enorme
