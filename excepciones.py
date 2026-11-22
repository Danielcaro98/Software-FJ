
from datetime import datetime
from pathlib import Path


# Excepcion general
class SoftwareFJError(Exception):
    pass


class DatoInvalidoError(SoftwareFJError):
    pass


class ParametroFaltanteError(SoftwareFJError):
    pass


class OperacionNoPermitidaError(SoftwareFJError):
    pass


class ReservaIncorrectaError(SoftwareFJError):
    pass


class ServicioNoDisponibleError(SoftwareFJError):
    pass


class CalculoInconsistenteError(SoftwareFJError):
    pass


# Registrar errores en archivo
def registrar_error_log(error, archivo_log="logs.txt"):

    ruta = Path(__file__).resolve().parent / archivo_log

    try:
        with open(ruta, "a", encoding="utf-8") as archivo:

            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            archivo.write(
                f"[{fecha}] {type(error).__name__}: {error}\n"
            )

    except OSError as error_archivo:
        raise OperacionNoPermitidaError(
            "Error writing to log file"
        ) from error_archivo


# Ejecutar validaciones
def ejecutar_validacion_encadenada(accion):

    try:
        resultado = accion()

    except ValueError as error:

        nuevo_error = DatoInvalidoError(
            "Invalid data detected"
        )

        nuevo_error.__cause__ = error

        registrar_error_log(nuevo_error)

        raise nuevo_error from error

    except SoftwareFJError as error:

        registrar_error_log(error)
        raise

    else:
        return resultado

    finally:
        pass
