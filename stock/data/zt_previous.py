from typing import List
import akshare as ak
from pathlib import Path
from datetime import datetime,timedelta
from loguru import logger
import yagmail



tasks = [
    ak.stock_em_zt_pool,
    ak.stock_em_zt_pool_dtgc,
    ak.stock_em_zt_pool_zbgc,
    ak.stock_em_zt_pool_previous,
    ak.stock_em_zt_pool_strong,
    ak.stock_em_zt_pool_sub_new,
    ak.stock_zh_a_alerts_cls,
    ak.stock_zh_a_spot,
]


