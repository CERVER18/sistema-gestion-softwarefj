import logging
import os

# Aseguramos que la carpeta logs exista
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename='logs/sistema_fj.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def registrar_log(mensaje, nivel="info"):
    if nivel == "info": logging.info(mensaje)
    elif nivel == "error": logging.error(mensaje)
    elif nivel == "warning": logging.warning(mensaje)
    elif nivel == "critical": logging.critical(mensaje)
