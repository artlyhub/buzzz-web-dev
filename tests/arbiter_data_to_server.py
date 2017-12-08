import pandas as pd
import os

from arbiter.models import (
    BTC,
    BCH,
    ETH,
    ETC,
    XRP,
)

coins_list = ['btc', 'bch', 'eth', 'etc', 'xrp']

tests_path = os.getcwd() + '\\tests\\coin_data'
os.chdir(tests_path)
data_files = os.listdir()

for coin in coins_list:
    csv_file = [data_file for data_file in data_files if coin in data_file][0]
    coin_data = pd.read_csv(csv_file.format(), encoding='euc-kr')

    for coin_id in range(len(coin_data)):
        coin_d = coin_data.ix[coin_id]
        code = str(coin_d['code']).zfill(6)
        date = coin_d['date']
        name = coin_d['name']
        market_type = coin_d['market_type']
        ticker_inst = Ticker(code=code,
                             date=date,
                             name=name,
                             market_type=market_type)
        ticker_inst.save()
        print(code + ' saved.')
