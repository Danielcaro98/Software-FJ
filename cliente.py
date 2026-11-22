
from entidad import Entidad
from excepciones import ErrorCliente
from registros import registrar_evento, registrar_error

class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):

        super().__init__(identificacion)

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        self.validar_datos()

    # validar informacion del cliente
    def validar_datos(self):

        if not self.__nombre.strip():
            raise ValueError("Customer name cannot be empty")

        if "@" not in self.__correo or "." not in self.__correo:
            raise ValueError("Invalid email address")

        if not self.__telefono.isdigit():
            raise ValueError("Phone must contain only numbers")

        if len(self.__telefono) < 7 or len(self.__telefono) > 15:
            raise ValueError("Invalid phone number")

    #consultar nombre
    def obtener_nombre(self):
        return self.__nombre

    #mostrar informacion
    def mostrar_informacion(self):

        return(
            f"ID:{self.obtener_identificador()}\n"
            f"Name: {self.__nombre}\n"
            f"Email: {self.__correo}\n"
            f"Phone: {self.__telefono}"
        )
