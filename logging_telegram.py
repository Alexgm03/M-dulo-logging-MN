import logging
import requests

TOKEN = "TU_TOKEN"
CHAT_ID = "TU_CHAT_ID"


class TelegramHandler(logging.Handler):

    def emit(self, record):

        mensaje = self.format(record)

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        requests.post(
            url,
            data={
                "chat_id": CHAT_ID,
                "text": mensaje
            }
        )


logger = logging.getLogger("Telegram")

logger.setLevel(logging.DEBUG)

telegram = TelegramHandler()

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s",
    "%d/%m/%Y %H:%M:%S"
)

telegram.setFormatter(formatter)

logger.addHandler(telegram)

logger.info("Este mensaje llegó a Telegram")
logger.error("Error enviado por Telegram")