from typing import Any

import akshare as ak
import pandas as pd

from stock.data.data import Data
from stock.utils import *


@register.register("raw_data")
class RawData(Data):
    # 获取原始数据
    def __init__(self, date):
        super().__init__(date)

    def get_data(self) -> Any:
        stock_zh_a_spot_df: pd.DataFrame = ak.stock_zh_a_spot()
        return stock_zh_a_spot_df

    def save(self, obj):
        if isinstance(obj, pd.DataFrame):
            obj.to_csv(f"./raw_data/{self.date}.csv", index=False, encoding="utf-8")
