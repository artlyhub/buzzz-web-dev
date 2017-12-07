import os, requests
import pandas as pd

buzzz_url = 'http://45.32.63.193/api/ohlcv/'
dest_path = os.getcwd() + '\\tests'

def get_buzzz_data(buzzz_url):
    r = requests.get(buzzz_url)
    if r.status_code == 200:
        data = r.json()
        df = pd.DataFrame(data['results'])
        prev_url = data['previous']
        next_url = data['next']
        print(buzzz_url)
    return df, prev_url, next_url

df, prev_url, next_url = get_buzzz_data(buzzz_url)
while next_url != None:
    buzzz_url = next_url
    temp_df, prev_url, next_url = get_buzzz_data(buzzz_url)
    df = df.append(temp_df, ignore_index=True)
df.to_csv(dest_path + '\\{}.csv'.format('ohlcv'), index=False)
