from stock.sentiment.sentiment_analyse import sentiment_analyse
from stock.utils import is_trade_day, logger, register
import stock.data


class Sentiment:

    def run(self):
        if is_trade_day:
            logger.info("today is trade_date")
            logger.info(f"{register.keys()}")
            for i in register.keys():
                # logger.info(dir(register[i]))
                register[i].get_save_data()
            # sentiment_analyse.run()
            logger.info('结束')
        else:
            logger.info("不是交易日，略过")
