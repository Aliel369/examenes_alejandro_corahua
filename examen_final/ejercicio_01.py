"""
Ejercicio 01: Sistema de alquiler de vehículos.
"""


class Vehiculo:
    def __init__(self, marca, modelo, anio=2020):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def actualizar_marca(self, nueva_marca):
        self.marca = nueva_marca

    def actualizar_anio(self, nuevo_anio):
        if nuevo_anio > 0:
            self.anio = nuevo_anio
        else:
            print("Error: El año debe ser mayor que cero.")

    def mostrar_datos(self):
        print("Datos del vehículo")
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}")

class VehiculoAlquiler(Vehiculo):
    def __init__(self, marca, modelo, anio, codigo, tarifa_diaria):
        super().__init__(marca, modelo, anio)
        self.codigo = codigo
        self.__tarifa_diaria = 0.0 # Encapsulamos el atributo
        self.actualizar_tarifa(tarifa_diaria)

    @property
    def tarifa_diaria(self):
        return self.__tarifa_diaria

    def actualizar_tarifa(self, nueva_tarifa):
        if nueva_tarifa > 0:
            self.__tarifa_diaria = nueva_tarifa
        else:
            print(f"(Atención) Intento de asignación de una nueva tarifa es inválida ({nueva_tarifa}). La tarifa no fue modificada.")

    def aumentar_tarifa(self, porcentaje=10):
        incremento = self.__tarifa_diaria * (porcentaje / 100)
        self.__tarifa_diaria += incremento

    def calcular_descuento(self, dias_alquiler):
        importe_total = self.__tarifa_diaria * dias_alquiler

        if dias_alquiler < 2:
            porcentaje_desc = 5
        elif 2 <= dias_alquiler <= 5:
            porcentaje_desc = 10
        else:
            porcentaje_desc = 15

        monto_descuento = importe_total * (porcentaje_desc / 100)
        total_final = importe_total - monto_descuento

        return importe_total, porcentaje_desc, total_final


if __name__ == "__main__":
    print("=== Prueba del Sistema De Alquiler De Vehículos ===")

    # Creamos dos vehículos diferentes
    v1 = VehiculoAlquiler("Toyota", "Corolla", 2022, "A001", 100.0)
    v2 = VehiculoAlquiler("Hyundai", "Sonata", 2018, "A002", 80.0)

    print("\n--- 1. Datos iniciales y prueba de tarifas ---")
    v1.mostrar_datos()
    print(f"Código: {v1.codigo} ; Tarifa inicial: S/. {v1.tarifa_diaria:.2f}")

    # Incremento de las tarifas
    print("\nAplicando dos incrementos consecutivos a v1")
    v1.aumentar_tarifa(10)  # 100 -> 110
    v1.aumentar_tarifa(15)  # 110 -> 126.50
    print(f"Tarifa actualizada de v1: S/. {v1.tarifa_diaria:.2f}")

    # Verificación de tarifa negativa
    print("\n--- 2. Intento de asignar una tarifa negativa ---")
    v1.actualizar_tarifa(-50.0)
    print(f"Tarifa actual tras el intento fallido: S/. {v1.tarifa_diaria:.2f}")

    # Calculos de descuentos e importes finales
    print("\n--- 3. Cálculo de descuentos ---")
    dias_pruebas = [1, 3, 7]
    for dias in dias_pruebas:
        importe, desc, total = v1.calcular_descuento(dias)
        print(f"Vehículo: {v1.marca} {v1.modelo} ; Días: {dias}")
        print(f"  > Importe antes del descuento: S/. {importe:.2f}")
        print(f"  > Descuento aplicado: {desc}%")
        print(f"  > Total final a pagar: S/. {total:.2f}\n")