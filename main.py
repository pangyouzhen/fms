from loguru import logger
from stock.data.data import Data
from stock.utils import *
from stock.sentiment.sentiment import Sentiment
from stock.utils.register import *


def main():
    logger.info("程序开始运行")

    sentiment = Sentiment()
    sentiment.run()


if __name__ == '__main__':
    main()
