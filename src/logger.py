import logging


format = "%(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(
    format=format,
    encoding="utf-8",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)