"""
Ejercicio 02: Transferencias entre personas
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

    """Método para registrar el nombre, edad y saldo de la persona con validación de errores"""
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

        #Transfiero la clase del primer ejercicio ya que este ejercicio lo requiere, pero solo trabajare con el saldo
        #Uso las mismas condiciones que use para la edad, para que el monto del saldo sea valido
        while True:
            try:
                self.saldo = float(input("Ingrese el saldo de la persona: "))
                if self.saldo < 0:
                    print("Error: El saldo no puede ser un número negativo. Ingrese un dato válido.")
                    continue
                break
            except ValueError:
                print("Error: Debe ingresar un valor numérico para el saldo. Ingrese un dato válido.")

    """Método para consultar el saldo actual de la persona"""
    def consultar_saldo(self):
        print("El saldo actual de {} es: ${:.2f}".format(self.nombre, self.saldo))

    """Método para efectuar una transferencia de dinero de una persona a otra"""
    def transferir(self, destinatario, monto):
        try:
            # Se valida que el monto sea de tipo numérico y mayor a cero
            if not isinstance(monto, (int, float)) or monto <= 0:
                print("Error: El monto a transferir debe ser un valor numérico mayor a cero.")
                return False

            # Se valida si el saldo disponible es suficiente
            if monto > self.saldo:
                print("Error: Operación rechazada. {} no cuenta con saldo suficiente (${:.2f}) para transferir ${:.2f}.".format(
                    self.nombre, self.saldo, monto
                ))
                return False

            # Se efectúa la transferencia: se descuenta al emisor y se suma al receptor
            self.saldo -= monto
            destinatario.saldo += monto
            print("¡Transferencia exitosa! {} ha transferido ${:.2f} a la cuenta de {}.".format(
                self.nombre, monto, destinatario.nombre
            ))
            return True

        except Exception as e:
            print("Ocurrió un error inesperado durante la transferencia: {}".format(e))
            return False

    """Método para incrementar la edad en un año cada vez que se invoque."""
    def cumpleanos(self):
        self.edad += 1
        print("¡Happy Birthday To You, {}! Has cumplido {} años.".format(self.nombre, self.edad))


if __name__ == "__main__":
    print("=" * 50)
    print("Sistema de transferencias")
    print("=" * 50)

    # Crear dos objetos de la clase Persona
    persona_1 = Persona()
    persona_1.registrar_datos()

    persona_2 = Persona()
    persona_2.registrar_datos()

    print("=" * 50)
    print("Consulta de saldos iniciales")
    print("=" * 50)
    persona_1.consultar_saldo()
    persona_2.consultar_saldo()

    # Aquí se realizarán las pruebas mencionadas, se harán 2 inválidas y 1 válida
    print("=" * 50)
    print("Prueba 1: Intento de transferencia rechazado (saldo insuficiente)")
    print("=" * 50)
    # Intento de transferir un monto mayor al saldo que posee persona_1
    monto_excesivo = persona_1.saldo + 500.0
    print("Intentando transferir ${:.2f} de {} a {}...".format(monto_excesivo, persona_1.nombre, persona_2.nombre))
    persona_1.transferir(persona_2, monto_excesivo)

    print("=" * 50)
    print("Prueba 2: Intento de transferencia rechazado (monto menor o igual a cero)")
    print("=" * 50)
    print("Intentando transferir un monto inválido (-30.0)...")
    persona_1.transferir(persona_2, -30.0)

    print("=" * 50)
    print("Prueba 3: Transferencia válida exitosa")
    print("=" * 50)

    # Realizamos una transferencia con un monto válido dentro del saldo disponible
    monto_valido = 100.0
    print("Intentando transferir ${:.2f} de {} a {}...".format(monto_valido, persona_1.nombre, persona_2.nombre))
    persona_1.transferir(persona_2, monto_valido)

    print("=" * 50)
    print("Saldos finales actualizados")
    print("=" * 50)
    persona_1.consultar_saldo()
    persona_2.consultar_saldo()
    print("=" * 50)