
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
	OPEN = False
	#오늘 날짜
	today_date = datetime.now().strftime('%Y%m%d')
	#ticker가져오기
	ticker = Ticker.objects.filter(date=today_date)
	#오늘 ohlcv 가져오기(중복방지)
	ohlcv = OHLCV.objects.filter(date=today_date)

	#장 열었는지 확인(평일인데 안여는 날 제외)
	url = "http://finance.naver.com/item/sise_day.nhn?code="+ticker[100].code
	user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
	r = requests.get(url, headers= user_agent, auth=('user', 'pass'))
	d = r.text
	soup = BeautifulSoup(d, "html.parser")
	market_date = soup.find('span', {'class':'tah p10 gray03'}).string.raplace(".", "")
	if (market_date == today_date):
		OPEN = True

	if (OPEN):
		ohlcv_list = []
		for i in range(len(ticker)):
			#이미 저장 되었으면 pass
			if not(ohlcv.filter(code=ticker[i].code).exists()):
				url = "http://finance.naver.com/item/sise_day.nhn?code="+ticker[i].code
				print(url)
				df = pd.read_html(url, thousands='')

				open_price = int(df[0].ix[1][3].replace(",", ""))
				high_price = int(df[0].ix[1][4].replace(",", ""))
				low_price = int(df[0].ix[1][5].replace(",", ""))
				close_price = int(df[0].ix[1][1].replace(",", ""))
				volume = int(df[0].ix[1][6].replace(",", ""))

				data = OHLCV(code=ticker[i].code, date=today_date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price, volume=volume)
				ohlcv_list.append(data)
				print(str(i)+ ' added ' + ticker[i].code + ' data')
		OHLCV.objects.bulk_create(ohlcv_list)
		print("all process done successfully!")



get_ohlcv()
