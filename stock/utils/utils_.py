from pathlib import Path
from stock.utils.logger_utils import logger

path = Path("./")
logger.info(f"当前的路径是{path.absolute()}")
