from typing import Optional

from stock.utils import logger

class Data:
    def __init__(self, date: Optional[str]):
        super().__init__()
        if date is None:
            date = date
        self.date = date

    @logger.catch
    def get_data(self):
        raise NotImplementedError

    @logger.catch
    def save(self, obj):
        raise NotImplementedError

    @logger.catch
    def save_sql(self):
        pass

    @logger.catch
    def run(self):
        obj = self.get_data()
        if obj:
            return self.save(obj)
