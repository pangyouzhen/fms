from stock.utils.logger_utils import logger
from stock.utils.register import Register
from stock.utils.datetime_utils import date, last_trade, is_trade_day

logger = logger
register = Register("data")
is_trade_day = is_trade_day
date = date
last_trade = last_trade
