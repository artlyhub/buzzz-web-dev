from __future__ import absolute_import, unicode_literals
import requests
import random
import time
from datetime import datetime
import simplejson as json
from celery.decorators import task
    
@task(name="sum_two_numbers")
def add(x, y):
    return x + y

@task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total

@task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)

# from arbiter.models import (
#     BTC,
#     BCH,
#     ETH,
#     ETC,
#     XRP,
# )
#
# coins_list = ('btc', 'bch', 'eth', 'etc', 'xrp',)
# coins_model = {
#     'btc': BTC,
#     'bch': BCH,
#     'eth': ETH,
#     'etc': ETC,
#     'xrp': XRP
# }

# @task(name="coinone_get_base_orderbook")
# def coinone_orderbook():
#     starting_time = time.time()
#     coinone_url = 'https://api.coinone.co.kr/orderbook/'
#     for coin in coins_list:
#         data = {
#             'currency': coin
#         }
#         r = requests.get(coinone_url, data=json.dumps(data))
#     data = {'status': r.status_code, 'time': r.json()['timestamp'], 'ask': r.json()['ask'][0], 'bid': r.json()['bid'][0]}
#     record = CoinPriceRecord(date='20170101', price_record=data)
#     record.save()

# @task(name="bithumb_get_base_orderbook")
# def bt_orderbook():
#     start_time = time.time()
#     success = False
#     datetime_format = '%Y%m%d%H:%M:%S'
#     for coin in coins_list:
#         bithumb_url = 'https://api.bithumb.com/public/orderbook/{}/?count=1'.format(coin)
#         r = requests.get(bithumb_url)
#         if r.status_code == 200:
#             data = r.json()
#             r_timestamp = data['data']['timestamp']
#             r_datetime = datetime.fromtimestamp(int(r_timestamp)/1000).strftime(datetime_format)
#             date = r_datetime[:8]
#             time_data = r_datetime[8:]
#             ask = int(data['data']['asks'][0]['price'])
#             bid = int(data['data']['bids'][0]['price'])
#             record = coins_model[coin](date=date,
#                                        time=time_data,
#                                        ask=ask,
#                                        bid=bid)
#             record.save()
#     success = True
#     end_time = time.time()
#     return success, 'Process time: {}'.format(str(end_time - start_time))

# @task(name="bithumb_get_recent_transactions")
# def bt_transactions():
