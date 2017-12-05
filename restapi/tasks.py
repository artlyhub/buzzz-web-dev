
from restapi.models import Ticker
from restapi.models import OHLCV
from datetime import datetime
import pandas as pd
from bs4 import BeautifulSoup
import requests
import simplejson as json
from celery.decorators import task





@task(name="scrape_naver_ohlcv")
def get_ohlcv():
	#오늘 날짜
	date = datetime.now().strftime('%Y%m%d')
	#ticker가져오기
	ticker = Ticker.objects.filter(date=date)

	for i in range(len(ticker)):
		if not(OHLCV.objects.filter(code=ticker[i].code).filter(date=date).exists()):
			#OHLCV
			url = "http://finance.naver.com/item/sise_day.nhn?code="+str(ticker[i].code) 
			df = pd.read_html(url, thousands='')
			
			open_price = int(df[0].ix[1][3].replace(",", ""))
			high_price = int(df[0].ix[1][4].replace(",", ""))
			low_price = int(df[0].ix[1][5].replace(",", ""))
			close_price = int(df[0].ix[1][1].replace(",", ""))
			volume = int(df[0].ix[1][6].replace(",", ""))

			data = OHLCV(code=ticker[i], date=date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price, volume=volume)
			data.save()















