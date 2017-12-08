import pandas as pd
import os

from restapi.models import Ticker, OHLCV

tests_path = os.getcwd() + '\\tests'

ohlcv_data = pd.read_csv(tests_path + '\\ohlcv.csv')

for index in range(len(ohlcv_data)):
    ohlcv = ohlcv_data.ix[index]
    code = Ticker.objects.filter(id=ohlcv['code']).first()
    date = str(ohlcv['date'])
    open_price = int(ohlcv['open_price'])
    high_price = int(ohlcv['high_price'])
    low_price = int(ohlcv['low_price'])
    close_price = int(ohlcv['close_price'])
    volume = int(ohlcv['volume'])
    ohlcv_inst = OHLCV(code=code,
                       date=date,
                       open_price=open_price,
                       high_price=high_price,
                       low_price=low_price,
                       close_price=close_price,
                       volume=volume)
    ohlcv_inst.save()
    print(code.code + ' ' + date + ' saved.')
