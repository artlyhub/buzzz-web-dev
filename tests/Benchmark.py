## @Ver     0.8v
## @Author  Phillip Park
## @Date    2017/12/12
## @Details 벤치마크 데이터 관리

import pandas as pd
import pandas_datareader as wb
import os, datetime


class Benchmark:
    def __init__(self):
        self.DEST = os.getcwd() + '\\data\\bm'

    def _init(self, year=1990, month=1, day=1):
        start = datetime.datetime(year, month, day)
        end = datetime.datetime.now()
        df_null = wb.DataReader("^KS11", "yahoo", start, end)
        self.df = df_null.dropna()

    def get(self):
        f = self.DEST + '\\BM.csv'
        if os.path.exists(f):
            self.df = pd.read_csv(f):
            return self.df
        else:
            print('BM data does not exist locally, retrieving data')
            self._init()
            print('Retrieved')
            return self.df

    def save(self):
        self.df.to_csv(self.DEST + '\\BM.csv')
