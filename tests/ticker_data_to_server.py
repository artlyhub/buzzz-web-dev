import pandas as pd
import os

from restapi.models import Ticker

tests_path = os.getcwd() + '\\tests'

ticker_data = pd.read_csv(tests_path + '\\ticker.csv', encoding='euc-kr')

for ticker_id in range(len(ticker_data)):
    ticker = ticker_data.ix[ticker_id]
    code = str(ticker['code']).zfill(6)
    date = ticker['date']
    name = ticker['name']
    market_type = ticker['market_type']
    ticker_inst = Ticker(code=code,
                         date=date,
                         name=name,
                         market_type=market_type)
    ticker_inst.save()
    print(code + ' saved.')
