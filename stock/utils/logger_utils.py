from loguru import logger
from datetime_utils import date

logger.add(f"/data/project/stock/log/runtime_{date}.log", rotation="1 week")
