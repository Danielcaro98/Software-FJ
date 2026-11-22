from entidad import Entidad
from abc import abstractmethod


# Clase abstracta Servicio
class Servicio(Entidad):

    def __init__(self, identificador, nombre, precio_base):

        super().__init__(identificador)

        self._nombre = nombre
        self._precio_base = precio_base

        self.validar_parametros()

    # Validar datos del servicio
    def validar_parametros(self):

        if not self._nombre.strip():
            raise ValueError("Service name cannot be empty")

        if self._precio_base <= 0:
            raise ValueError("Base price must be greater than zero")

    # Metodo para calcular costos
    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    # Metodo para describir el servicio
    @abstractmethod
    def describir_servicio(self):
        pass

    # Mostrar informacion
    def mostrar_informacion(self):

        return (
            f"Service ID: {self.obtener_identificador()}\n"
            f"Name: {self._nombre}\n"
            f"Base Price: ${self._precio_base}"
        )


class ReservaSala(Servicio):

    def __init__(self, identificador, nombre, precio_base, capacidad):

        super().__init__(identificador, nombre, precio_base)

        self.capacidad = capacidad

        if self.capacidad <= 0:
            raise ValueError("Capacity must be greater than zero")

    def calcular_costo(self, duracion):

        return self._precio_base * duracion

    def describir_servicio(self):

        return f"Room reservation: {self._nombre}. Capacity: {self.capacidad} people."


class AlquilerEquipos(Servicio):

    def __init__(self, identificador, nombre, precio_base, cantidad):

        super().__init__(identificador, nombre, precio_base)

        self.cantidad = cantidad

        if self.cantidad <= 0:
            raise ValueError("Quantity must be greater than zero")

    def calcular_costo(self, duracion):

        return self._precio_base * duracion * self.cantidad

    def describir_servicio(self):

        return f"Equipment rental: {self._nombre}. Quantity: {self.cantidad}."


class Asesoria(Servicio):

    def __init__(self, identificador, nombre, precio_base, especialidad):

        super().__init__(identificador, nombre, precio_base)

        self.especialidad = especialidad

        if not self.especialidad.strip():
            raise ValueError("Specialty cannot be empty")

    def calcular_costo(self, duracion):

        return self._precio_base * duracion

    def describir_servicio(self):

        return f"Specialized consulting: {self._nombre}. Specialty: {self.especialidad}."


# Pruebas de servicios

try:

    sala = ReservaSala("S01", "Meeting Room", 30000, 10)

    equipos = AlquilerEquipos("E01", "Computers", 15000, 2)

    asesoria = Asesoria("A01", "Technical Support", 50000, "Systems")

    print(sala.describir_servicio())
    print("Cost:", sala.calcular_costo(3))

    print(equipos.describir_servicio())
    print("Cost:", equipos.calcular_costo(3))

    print(asesoria.describir_servicio())
    print("Cost:", asesoria.calcular_costo(2))

except ValueError as error:

    print("Error:", error)
