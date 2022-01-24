import json
from datetime import datetime

import pandas as pd
import requests

from stock.data.cls.cls import *
from stock.data.data import Data
from stock.utils import *


@register.register("cls_alter")
class ClsAlterCsv(Data):
    def __init__(self, date: str):
        super().__init__(date)

    def get_data(self):
        payload = json.dumps(
            {
                "type": "telegram",
                "keyword": "快讯",
                "page": 0,
                "rn": 30,
                "os": "web",
                "sv": "7.2.2",
                "app": "CailianpressWeb",
            }
        )
        today = datetime.today()
        today_start = today.replace(hour=0, minute=0, second=0, microsecond=0)
        response = requests.request("POST", cls_url, headers=cls_headers, data=payload)
        res = response.json()
        data = res["data"]["telegram"]["data"]
        df = pd.DataFrame(data)
        df = df[["descr", "id", "time"]]
        df["descr"] = df["descr"].astype(str).str.replace("</em>", "")
        df["descr"] = df["descr"].str.replace("<em>", "")
        df["time"] = df["time"].apply(datetime.fromtimestamp)
        df = df[df["time"] > today_start]
        df.columns = ["快讯信息", "id", "时间"]
        self.df = df
        return self.df

    def save(self, **kwargs):
        self.df.to_csv(f"./raw_data/qucik_{date}.txt", encoding="utf-8")
