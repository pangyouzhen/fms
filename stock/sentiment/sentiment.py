from stock.sentiment.sentiment_analyse import SentimentAnalyse
from stock.utils import is_trade_day, logger, register


class Sentiment:

    def __init__(self) -> None:
        self.sentiment_analyse = SentimentAnalyse()

    def run(self):
        if is_trade_day:
            logger.info("today is trade_date")
            logger.info(f"{register.keys()}")
            for i in register.keys():
                i.run()
            self.sentiment_analyse.run()
            logger.info('结束')
        else:
            logger.info("不是交易日，略过")
