"""
Ejercicio 3: Caso de Calculadora de propinas
"""

#1 Datos
total_cuenta = 300.0
porcentaje_propina = 6.7
numero_personas = 2

#2 Monto total y más la propina
monto_propina = total_cuenta * (porcentaje_propina / 100)
total_con_propina = total_cuenta + monto_propina
print("El monto total con propina es de: S/. {}".format(f"{total_con_propina:.2f}"))
print("-------------------")

#3 Monto que debe pagar cada persona
monto_persona = total_con_propina / numero_personas
print("Cada persona debe pagar: S/. {}".format(f"{monto_persona:.2f}"))
print("-------------------")

#4 Condicional si superan el monto de 100
if monto_persona > 100:
    print("¡Atención! El monto que debe pagar cada persona supera los S/. 100")
print("-------------------")

if monto_persona <= 100:
    print("El monto por persona no llega a superar los S/. 100")
