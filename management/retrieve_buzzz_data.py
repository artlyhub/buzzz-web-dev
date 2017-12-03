'''
Retrieve data from Buzzz server/Arbiter API
BTC, BCH, ETH, ETC, XRP price data
'''
import os, datetime, requests
import pandas as pd

coins_list = ['btc', 'bch', 'eth', 'etc', 'xrp']

dest_path = os.getcwd() + '\\coin_data'
today_date = datetime.datetime.now().strftime('%Y%m%d')

def get_buzzz_data(buzzz_url):
    r = requests.get(buzzz_url)
    if r.status_code == 200:
        data = r.json()
        df = pd.DataFrame(data['results'])
        prev_url = data['previous']
        next_url = data['next']
        print(buzzz_url)
    return df, prev_url, next_url

for coin in coins_list:
    buzzz_url = 'https://buzzz.co.kr/arbiter-api/{}/order/'.format(coin)
    df, prev_url, next_url = get_buzzz_data(buzzz_url)
    while next_url != None:
        buzzz_url = next_url
        temp_df, prev_url, next_url = get_buzzz_data(buzzz_url)
        df = df.append(temp_df, ignore_index=True)
    df.to_csv(dest_path + '\\{}{}.csv'.format(coin, today_date), index=False)
