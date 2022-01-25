from typing import List

import arrow
import pandas as pd


class DateUtils:
    def __init__(self, input_date: str = None):
        """
        input_date: "2021-03-10"
        """
        # todo 检查输入的时间格式
        if input_date:
            self.input_date: str = input_date
        else:
            self.input_date: str = arrow.now().format("YYYY-MM-DD")
        self.trade_date_list: List[str] = self.get_trade_list()
        self.last_trade_date = self.get_last_trade_date()
        self.is_trade_date = self.today_is_trade_date()

    def get_trade_list(self) -> List[str]:
        trade_date_df = pd.read_csv('/data/project/fms/stock/utils/other/tool_trade_date_hist_sina_df.csv')
        return trade_date_df["trade_date"].tolist()

    # 获取上一个交易日
    def get_last_trade_date(self) -> str:
        ind = self.trade_date_list.index("%s" % self.input_date)
        return self.trade_date_list[ind - 1]

    # 判断是不是交易日
    def today_is_trade_date(self):
        if self.input_date in self.trade_date_list:
            return True
        return False

input_date = DateUtils().input_date
last_trade = DateUtils().last_trade_date
is_trade_day = DateUtils().is_trade_date