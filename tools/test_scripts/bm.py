import pandas_datareader as wb
import datetime

from restapi.models import Ticker, OHLCV

start = datetime.datetime(1990, 1, 1)
end = datetime.datetime(2017, 12, 11)
df_null = wb.DataReader("^KS11", "yahoo", start, end)
df = df_null.dropna()

code = Ticker.objects.filter(code='BM').first()

for i in range(len(df)):
    row = df.ix[i]
    date = row.name.strftime('%Y%m%d')
    open_p = int(row['Open'])
    high = int(row['High'])
    low = int(row['Low'])
    close = int(row['Adj Close'])
    volume = int(row['Volume'])
    data = OHLCV(code=code,
                 date=date,
                 open_price=open_p,
                 high_price=high,
                 low_price=low,
                 close_price=close,
                 volume=volume)
    data.save()
    print(date + ' saved')
