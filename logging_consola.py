import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(filename)s | %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S"
)

logging.debug("Mensaje DEBUG")
logging.info("Mensaje INFO")
logging.warning("Mensaje WARNING")
logging.error("Mensaje ERROR")
logging.critical("Mensaje CRITICAL")