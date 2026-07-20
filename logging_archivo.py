import logging

logging.basicConfig(
    filename="logs.log",
    filemode="a",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(filename)s | %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S"
)

logging.info("Programa iniciado")
logging.warning("Advertencia")
logging.error("Ha ocurrido un error")