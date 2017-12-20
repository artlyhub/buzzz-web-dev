
from management.common_function import end_point_check

from restapi.models import Ticker
from restapi.models import OHLCV
from datetime import datetime
import pandas as pd
from bs4 import BeautifulSoup
import requests
# import simplejson as json
# from celery.decorators import task
import time



# url = "http://finance.naver.com/item/sise_day.nhn?code=011300"
# print(url)
# df = pd.read_html(url, thousands='')
#
# open_price = int(df[0].ix[1][3].replace(",", ""))
# high_price = int(df[0].ix[1][4].replace(",", ""))
# low_price = int(df[0].ix[1][5].replace(",", ""))
# close_price = int(df[0].ix[1][1].replace(",", ""))
# volume = int(df[0].ix[1][6].replace(",", ""))
# print (open_price)
# print(high_price)
# print(low_price)
# print(close_price)
# print(volume)
#


def get_ohlcv():
	#오늘 날짜
	date = datetime.now().strftime('%Y%m%d')
	#ticker가져오기
	ticker = Ticker.objects.filter(date=date)
	#오늘 ohlcv 가져오기(중복방지)
	ohlcv = OHLCV.objects.filter(date=date)

	ohlcv_list = []
	for i in range(len(ticker)):
		if not(ohlcv.filter(code=ticker[i].code).exists()):
			#OHLCV
			url = "http://finance.naver.com/item/sise_day.nhn?code="+str(ticker[i].code)
			print(url)
			df = pd.read_html(url, thousands='')

			open_price = int(df[0].ix[1][3].replace(",", ""))
			high_price = int(df[0].ix[1][4].replace(",", ""))
			low_price = int(df[0].ix[1][5].replace(",", ""))
			close_price = int(df[0].ix[1][1].replace(",", ""))
			volume = int(df[0].ix[1][6].replace(",", ""))

			data = OHLCV(code=ticker[i].code, date=date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price, volume=volume)
			ohlcv_list.append(data)
			print('added ' + ticker[i].code + ' data')
	OHLCV.objects.bulk_create(ohlcv_list)
	print("all process done successfully!")


get_ohlcv()
