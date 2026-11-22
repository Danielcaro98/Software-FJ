import logging
from pathlib import Path

# Ruta del archivo de registros
ruta_logs = Path(_file_).resolve().parent / "logs.txt"

# Configuracion del registro
logging.basicConfig(
    filename=ruta_logs,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Registrar eventos
def registrar_evento(mensaje):
    logging.info(mensaje)


# Registrar errores
def registrar_error(mensaje):
    logging.error(mensaje)
