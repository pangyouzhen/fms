import akshare as ak

from stock.data.data import Data
from stock.utils import *


# @register.register("zt_data")
class ZtData(Data):
    # 获取原始数据
    def __init__(self, date):
        super().__init__(date)

    def get_data(self):
        today = date.replace("-", "")
        self.stock_em_zt_pool_df = ak.stock_em_zt_pool(today)

    def save(self,obj):
        self.stock_em_zt_pool_df.to_csv(f"stock_em_zt_pool_df_{date}.csv", encoding='utf-8')
