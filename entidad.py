from abc import ABC, abstractclassmethod

# clase abstracta
class Entidad(ABC):

    def __int__(self, identificador):
        self.__identificador = identificador


        # Metodo para consultar el idendificador
    def obtener_identificador(self):
         return self._identificador

        #metodo abstracto
    @abstractclassmethod
    def mostrar_informacion(self):
            pass