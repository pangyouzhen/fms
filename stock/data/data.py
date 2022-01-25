from stock.utils import input_date, logger

class Data:
    def __init__(self):
        super().__init__()
        self.date = input_date 

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
