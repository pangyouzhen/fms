import datetime
import math

import pandas as pd

from stock.utils import logger, date
from stock.utils.utils_ import path


class SentimentAnalyse:
    @logger.catch
    @staticmethod
    def high_open_ratio(df: pd.DataFrame):
        if df["昨收"] == 0:
            return 0
        return (df["最高"] - df['昨收']) / df["昨收"] * 100

    # 新浪财经今日的数据进行处理
    @logger.catch
    def today_data(self):
        df = pd.read_csv("%s/%s.csv", encoding="utf-8")
        df["high_open_ratio"] = df.apply(self.high_open_ratio, axis=1)
        df["代码"] = df["代码"].astype(str)
        df["代码"] = df["代码"].str[2:]
        # 688 科创板数据
        df688 = df[df["代码"].str.startswith("688")]
        # 300 创业板数据
        df300 = df[df["代码"].str.startswith("300")]
        # 其他 主板数据
        df_main = df[(~df["代码"].str.startswith("300")) &
                     (~df["代码"].str.startswith("688"))]
        return df, df688, df300, df_main

    # 市场情绪监控数据处理
    @logger.catch
    def sentiment_data(self):
        # 读取创业板数据
        # 读取主板数据
        main_board = pd.read_csv("%s/stock.csv", index_col=0)
        # start_board = pd.read_csv(self.sentiment_data_path / "start%s.csv" % (self.dayint[0:4]), index_col=0)
        last_limit_up_df = pd.read_csv("%s/limit_up%s.csv", encoding="utf-8")
        return main_board, last_limit_up_df

    @logger.catch
    def get_sentiment(self, df_main: pd.DataFrame, main_stock: pd.DataFrame, last_limit_up_df):
        """
        :param df_main: 每日的交易数据
        :param main_stock: 历史的市场情绪监控表，
        """

        def get_limit_up_data(x):
            if math.isnan(x):
                x = 1
            else:
                x += 1
            return x

        # 上涨数据
        increase_main = df_main[(df_main["涨跌幅"] > 0)]
        # 下跌数据
        decrease_main = df_main[(df_main["涨跌幅"] < 0)]
        print(increase_main.shape[0], decrease_main.shape[0])
        # main_stock.loc["%s" % today_int, "红盘"] = increase_main.shape[0]
        # main_stock.loc["%s" % today_int, "绿盘"] = decrease_main.shape[0]
        # 涨停
        limit_up = df_main[(df_main["涨跌幅"] > 9.9) & (df_main["涨跌幅"] < 11)]
        # 默认的涨停天数是一天
        limit_up_df = pd.merge(limit_up, last_limit_up_df,
                               left_on="名称", right_on="名称", how="left")
        limit_up_df = limit_up_df[["名称", "连续涨停天数(天)"]]
        limit_up_df["连续涨停天数(天)"] = limit_up_df["连续涨停天数(天)"].apply(
            get_limit_up_data)
        limit_up_df["连续涨停天数(天)"] = limit_up_df["连续涨停天数(天)"].astype(int)
        limit_up_df.to_csv(f"{path}/limit_up%s.csv", index=False)
        # 跌停
        limit_down = (df_main[(df_main["涨跌幅"] < -9.9)
                              & (df_main["涨跌幅"] > -11)])
        # main_stock.loc["%s" % today_int, "涨停"] = limit_up.shape[0]
        # main_stock.loc["%s" % today_int, "跌停"] = limit_down.shape[0]
        # 炸板
        once_limit_up = df_main[(df_main["high_open_ratio"] > 9.9) & (
                df_main["high_open_ratio"] < 11)]
        once_limit_up_name = once_limit_up["名称"].tolist()
        limit_up_name = limit_up["名称"].tolist()
        once = [i for i in once_limit_up_name if i not in limit_up_name]
        # main_stock.loc["%s" % today_int, "炸板"] = len(once)
        # 3连板数据以上数据 及 3连板数据
        limit_up_df_three_above = limit_up_df[limit_up_df["连续涨停天数(天)"] > 3]
        # 3连板数据
        limit_up_df_three = limit_up_df[limit_up_df["连续涨停天数(天)"] == 3]
        # 2连板数据
        limit_up_df_two = limit_up_df[limit_up_df["连续涨停天数(天)"] == 2]
        # main_stock.loc["%s" % today_int, "2连板个股数"] = limit_up_df_two.shape[0]
        # main_stock.loc["%s" % today_int, "2连板个股"] = ";".join(limit_up_df_two["名称"].tolist())
        # 连板数据
        limit_up_df_one = limit_up_df[limit_up_df["连续涨停天数(天)"] == 1]
        limit_up_df_three_above["连续涨停天数(天)"] = limit_up_df_three_above["连续涨停天数(天)"].astype(
            str)
        limit_up_df_three_above["data"] = limit_up_df_three_above["名称"].str.cat(
            limit_up_df_three_above["连续涨停天数(天)"])
        # main_stock.loc["%s" % today_int, "连板个股数"] = limit_up_df_one.shape[0]
        today_df = pd.DataFrame(
            data={
                "红盘": increase_main.shape[0],
                "绿盘": decrease_main.shape[0],
                "涨停": limit_up.shape[0],
                "跌停": limit_down.shape[0],
                "炸板": len(once),
                "3连板以上个股数": limit_up_df_three_above.shape[0],
                "3连板以上个股": ";".join(limit_up_df_three_above["data"].tolist()),
                "3连板": limit_up_df_three.shape[0],
                "3连板个股": ";".join(limit_up_df_three["名称"].tolist()),
                "2连板": limit_up_df_two.shape[0],
                "2连板个股": ";".join(limit_up_df_two["名称"].tolist()),
                "连板": limit_up_df_one.shape[0],
            },
            index=[date]
        )
        main_stock = main_stock.append(today_df)
        return main_stock

    @logger.catch
    def run(self):
        df, df688, df300, df_main = self.today_data(path)
        main_board, last_limit_up_df = self.sentiment_data()
        res = self.get_sentiment(df_main, main_board, last_limit_up_df)
        res.to_csv("%s/stock.csv", encoding="utf-8")


if __name__ == '__main__':
    input_date = datetime.date(year=2021, month=3, day=11)
    sentiment_analyse = SentimentAnalyse()
    sentiment_analyse.run()
