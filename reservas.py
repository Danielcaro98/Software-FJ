from cliente import Cliente
from servicios import Servicio, ReservaSala

class Reserva:

    def __init__(self, cliente, servicio, duracion):

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pending"

        self.validar_reserva()

    # Validar los datos de la reserva
    def validar_reserva(self):

        if not isinstance(self.__cliente, Cliente):
            raise ValueError("Invalid customer")

        if not isinstance(self.__servicio, Servicio):
            raise ValueError("Invalid service")

        if not isinstance(self.__duracion, (int, float)):
            raise ValueError("Duration must be a number")

        if isinstance(self.__duracion, bool) or self.__duracion <= 0:
            raise ValueError("Duration must be greater than zero")

    # Calcular costo de la reserva
    def calcular_total(self):

        return self.__servicio.calcular_costo(self.__duracion)

    # Confirmar reserva
    def confirmar_reserva(self):

        if self.__estado != "Pending":
            raise ValueError("Reservation cannot be confirmed")

        self.__estado = "Confirmed"

        return "Reservation confirmed successfully"

    # Cancelar reserva
    def cancelar_reserva(self):

        if self.__estado == "Cancelled":
            raise ValueError("Reservation is already cancelled")

        self.__estado = "Cancelled"

        return "Reservation cancelled successfully"

    # Procesar reserva
    def procesar_reserva(self):

        self.validar_reserva()

        if self.__estado != "Pending":
            raise ValueError("Only pending reservations can be processed")

        total = self.calcular_total()

        if not isinstance(total, (int, float)) or total <= 0:
            raise ValueError("Invalid reservation cost")

        mensaje = self.confirmar_reserva()

        return f"{mensaje}. Total: ${total:,.0f}"

    # Mostrar informacion de la reserva
    def mostrar_informacion(self):

        return (
            f"Customer: {self.__cliente.obtener_nombre()}\n"
            f"Service: {self.__servicio.describir_servicio()}\n"
            f"Duration: {self.__duracion} hours\n"
            f"Status: {self.__estado}\n"
            f"Total: ${self.calcular_total():,.0f}"
        )


# Prueba de la clase Reserva
if __name__ == "__main__":

    try:

        cliente1 = Cliente(
            "123456",
            "Daniel",
            "daniel@gmail.com",
            "3001234567"
        )

        sala1 = ReservaSala(
            "S01",
            "Meeting Room",
            30000,
            10
        )

        reserva1 = Reserva(cliente1, sala1, 3)

        print("BEFORE CONFIRMATION")
        print(reserva1.mostrar_informacion())

        print("\nPROCESS RESERVATION")
        print(reserva1.procesar_reserva())

        print("\nAFTER CONFIRMATION")
        print(reserva1.mostrar_informacion())

        print("\nCANCEL RESERVATION")
        print(reserva1.cancelar_reserva())

    except ValueError as error:
        print("Error:", error)
