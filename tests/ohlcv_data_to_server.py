import pandas as pd
import os

from restapi.models import Ticker, OHLCV

tests_path = os.getcwd() + '\\tests'

ohlcv_data = pd.read_csv(tests_path + '\\ohlcv.csv')

for index in range(len(ohlcv_data)):
    ohlcv = ohlcv_data.ix[index]
    code = Ticker.objects.filter(code=ohlcv['code']).first()
    date = ohlcv['date']
    open_price = ohlcv['open_price']
    high_price = ohlcv['high_price']
    low_price = ohlcv['low_price']
    close_price = ohlcv['close_price']
    volume = ohlcv['volume']
    ohlcv_inst = OHLCV(code=code,
                       date=date,
                       open_price=open_price,
                       high_price=high_price,
                       low_price=low_price,
                       close_price=close_price,
                       volume=volume)
    ohlcv_inst.save()
    print(code + ' ' + date + ' saved.')
