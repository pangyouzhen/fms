from typing import Optional
import akshare as ak

from stock.data.data import Data
from stock.utils import *


@register.register("zt_data")
class ZtData(Data):
    # 获取原始数据

    def __init__(self):
        super().__init__()
        
    def get_data(self):
        today = self.date.replace("-", "")
        self.stock_em_zt_pool_df = ak.stock_em_zt_pool(today)

    def save(self,obj):
        self.stock_em_zt_pool_df.to_csv(f"stock_em_zt_pool_df_{self.date}.csv", encoding='utf-8')
