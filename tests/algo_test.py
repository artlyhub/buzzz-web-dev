from restapi.models import Ticker, OHLCV
import numpy as np
import pandas as pd

ticker1 = Ticker.objects.all()[10]
ticker2 = Ticker.objects.all()[40]
ticker3 = Ticker.objects.all()[30]

ohlcv1 = list(OHLCV.objects.filter(code=ticker1).distinct('date').exclude(date__lte='20000100').values('date', 'close_price'))
ohlcv2 = list(OHLCV.objects.filter(code=ticker2).distinct('date').exclude(date__lte='20000100').values('date', 'close_price'))
ohlcv3 = list(OHLCV.objects.filter(code=ticker3).distinct('date').exclude(date__lte='20000100').values('date', 'close_price'))

df1 = pd.DataFrame(ohlcv1)
df1.set_index('date', inplace=True)
df1.rename(columns={'close_price': ticker1.code}, inplace=True)
df2 = pd.DataFrame(ohlcv2)
df2.set_index('date', inplace=True)
df2.rename(columns={'close_price': ticker2.code}, inplace=True)
df3 = pd.DataFrame(ohlcv3)
df3.set_index('date', inplace=True)
df3.rename(columns={'close_price': ticker3.code}, inplace=True)
# if len(df1) > len(df2):
#     method = 'left'
# else:
#     method = 'right'
# df = pd.merge(df1, df2, on='date', how=method)
df1 = pd.concat([df1, df2, df3], axis=1)
df1.index = pd.to_datetime(df1.index)
df1 = df1.pct_change()

print(df1['2017'])
