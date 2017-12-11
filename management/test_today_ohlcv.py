
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



def get_ohlcv():

	start_time = time.time()

	#오늘 날짜
	today_date = "20171211" #datetime.now().strftime('%Y%m%d')

	#ticker가져오기
	ticker = Ticker.objects.filter(date=today_date)

	#중단된 지점 확인 
	index = end_point_check("data\\"+today_date+"_daily_ohlcv_log.txt", ticker)
	index += 1 #다음 거부터 시작~

	#log 기록용
	f = open("data\\"+today_date+"_daily_ohlcv_log.txt", 'w')


	for i in range(index, len(ticker)):
		if not(OHLCV.objects.filter(code=ticker[i]).filter(date=today_date).exists()):
			#OHLCV
			url = "http://finance.naver.com/item/sise_day.nhn?code="+str(ticker[i].code) 
			df = pd.read_html(url, thousands='')
			if (str(df[0].ix[1][3]) == "nan"):
				open_price = 0
				high_price = 0
				low_price = 0
				close_price = 0
				volume = 0
			else:
				open_price = int(df[0].ix[1][3].replace(",", ""))
				high_price = int(df[0].ix[1][4].replace(",", ""))
				low_price = int(df[0].ix[1][5].replace(",", ""))
				close_price = int(df[0].ix[1][1].replace(",", ""))
				volume = int(df[0].ix[1][6].replace(",", ""))

			data = OHLCV(code=ticker[i], date=today_date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price, volume=volume)
			data.save()
		f.write(str(i)+" "+ticker[i].code+"\n")

	end_time = time.time()
	print(end_time-start_time)
	f.close()


get_ohlcv()






    
    
