"""
Ejercicio 01: Registro de personas
"""

from datetime import datetime

class Persona:
    """Atributo de clase para la nacionalidad"""
    nacionalidad = "Peruana"

    def __init__(self): # Se ponen los atributos vacíos para que sean insertados mediante la consola
        self.nombre = ""
        self.edad = 0
        self.saldo = 0.0
        self.fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M") # Para el registro de las personas con precisión en minutos

    """Metodo para registrar el nombre, edad y saldo de la persona y que se muestren las excepciones de errores """
    def registrar_datos(self):
        print("-" * 50)
        self.nombre = input("Ingrese el nombre de la persona: ")

        while True:
            try:
                self.edad = int(input("Ingrese la edad de la persona: "))
                if self.edad < 0:
                    print("Error: La edad no puede ser un número negativo. Ingrese un dato válido.")
                    continue
                break
            except ValueError:
                print("Error: Debe ingresar un número entero para la edad. Ingrese un dato válido.")

        self.saldo = float(input("Ingrese el saldo de la persona: "))

    """Metodo para incrementar la edad en un año."""
    def cumpleanos(self):
        self.edad += 1
        print("¡Happy Birthday To You, {}! Has cumplido {} años.".format(self.nombre, self.edad))

"""Función para mostrar el registro con precisión de minutos."""
def mostrar_fecha_registro(persona):
    print("{} fue registrado/a el: {}".format(persona.nombre, persona.fecha_registro))


if __name__ == "__main__":
    print("=" * 40)
    print("Sistema para el registro de personas")
    print("=" * 40)

    # Crear como mínimo dos objetos de la clase Persona
    persona_1 = Persona()
    persona_1.registrar_datos()

    persona_2 = Persona()
    persona_2.registrar_datos()

    print("=" * 40)
    print("Muestra de datos personales y el momento de registro")
    print("=" * 40)

    mostrar_fecha_registro(persona_1)
    print(" La edad actual de {} es de {} años, cuenta con un saldo de ${:.2f} y tiene nacionalidad: {}".format(
        persona_1.nombre, persona_1.edad, persona_1.saldo, persona_1.nacionalidad
    ))

    print("-" * 40)
    mostrar_fecha_registro(persona_2)
    print("La edad actual de {} es de {} años, cuenta con un saldo de ${:.2f} y tiene nacionalidad: {}".format(
        persona_2.nombre, persona_2.edad, persona_2.saldo, persona_2.nacionalidad
    )) #Los datos se muestran en una sola oración

    print("=" * 40)
    print("Aplicación del método cumpleaños")
    print("=" * 40)

    # Aplicación del metodo de cumpleaños a los 2 objetos
    persona_1.cumpleanos()
    persona_2.cumpleanos()

    print("=" * 40)
    print("Edades actualizadas")
    print("=" * 40)
    print("1. {}: {} años".format(persona_1.nombre, persona_1.edad))
    print("2. {}: {} años".format(persona_2.nombre, persona_2.edad))
    print("=" * 40)