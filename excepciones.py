
# Excepcion general del sistema
class ErrorSoftwareFJ(Exception):
    pass


# Error en los datos del cliente
class ErrorCliente(ErrorSoftwareFJ):
    pass


# Error en los servicios
class ErrorServicio(ErrorSoftwareFJ):
    pass


# Error en las reservas
class ErrorReserva(ErrorSoftwareFJ):
    pass


# Servicio no disponible
class ServicioNoDisponible(ErrorServicio):
    pass
