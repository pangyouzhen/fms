from loguru import logger
from stock.utils.datetime_utils import input_date

logger.add(f"/data/project/stock/log/runtime_{input_date}.log", rotation="1 week")
