from loguru import logger
from stock.utils.datetime_utils import date

logger.add(f"/data/project/stock/log/runtime_{date}.log", rotation="1 week")
