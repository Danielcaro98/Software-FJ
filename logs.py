
import logging

# Configurar el archivo donde se guardaran los registros
logging.basicConfig(
    filename="eventos.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Funcion para registrar eventos
def registrar_evento(mensaje):
    logging.info(mensaje)

# Funcion para registrar errores
def registrar_error(mensaje):
    logging.error(mensaje)
