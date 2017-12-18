import os
import pandas as pd
from restapi.models import OHLCV, Ticker, Info

DATA_DEST = os.getcwd() + '\\data'
OHLCV_DEST = os.getcwd() + '\\data\\ohlcv'

# requesting all values in Ticker table
if os.path.exists(DATA_DEST + '\\tickers.csv'):
    print('tickers.csv file exists, skipping')
    pass
else:
    tickers = list(Ticker.objects.all().values_list('code',
                                                    'date',
                                                    'name',
                                                    'market_type'))
    tickers = pd.DataFrame(tickers)
    tickers.to_csv(DATA_DEST + '\\tickers.csv', index=False, header=False)
    print('tickers.csv file saved')

if os.path.exists(DATA_DEST + '\\infos.csv'):
    print('infos.csv file exists, skipping')
    pass
else:
    infos = list(Info.objects.all().values_list('code__code',
                                                'date',
                                                'size_type',
                                                'style_type',
                                                'face_val',
                                                'stock_nums',
                                                'market_cap',
                                                'market_cap_rank',
                                                'industry',
                                                'per',
                                                'pbr',
                                                'yield_ret'))
    infos = pd.DataFrame(infos)
    infos.to_csv(DATA_DEST + '\\infos.csv', index=False, header=False)
    print('infos.csv file saved')

tickers = [ticker[0] for ticker in Ticker.objects.distinct('code').values_list('code')]

for ticker in tickers:
    if os.path.exists(OHLCV_DEST + '\\{}.csv'.format(ticker)):
        print('{}.csv file exists, skipping'.format(ticker))
        pass
    else:
        ohlcv_qs = OHLCV.objects.filter(code__code=ticker).distinct('date')
        ohlcv = list(ohlcv_qs.values_list('code__code',
                                     'date',
                                     'open_price',
                                     'high_price',
                                     'low_price',
                                     'close_price',
                                     'volume'))
        ohlcv_df = pd.DataFrame(ohlcv)
        ohlcv_df.to_csv(OHLCV_DEST + '\\{}.csv'.format(ticker), index=False, header=False)
        print('{}.csv file saved'.format(ticker))
