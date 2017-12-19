

from restapi.models import Ticker
from restapi.models import OHLCV
from datetime import datetime
import pandas as pd
from bs4 import BeautifulSoup
import requests
import lxml
import re
import time
import os


#오늘의 날짜
today_date = datetime.now().strftime("%Y%m%d")
#걸린 시간
av_time = 0
index = 0

ticker = [ticker.code for ticker in Ticker.objects.filter(market_type='KD')]

# for t in range(len(ticker)):
# 	code = Ticker.objects.filter(code=ticker[t]).first()
# 	print('Checking ' + code.code)
# 	ohlcv = OHLCV.objects.filter(date='20171208').filter(code=code)
# 	if ohlcv.exists():
# 		print('Exists....')
# 	else:
# 		print(code.code + '::::::')
# 		print("Doesn't exist, deleting all related data...")
# 		OHLCV.objects.filter(code=code).delete()

#log파일 열기
f = open("OHLCV_KD_log.txt", 'w')

#OHLCV
for t in range(len(ticker)):
	code = Ticker.objects.filter(code=ticker[t]).first()
	print('Checking ' + code.code)
	ohlcv = OHLCV.objects.filter(date='20171208').filter(code=code)
	if ohlcv.exists():
		print('Exists....')
	else:
		print(code.code + '::::::')
		print("Doesn't exist, deleting all related data...")
		OHLCV.objects.filter(code=code).delete()

		start_time = time.time()
		#log 기록(회사 code)
		f.write(ticker[t]+"\n")

		#사이트 html 가져오기
		url = "http://finance.naver.com/item/sise_day.nhn?code="+ticker[t]
		user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
		r = requests.get(url, headers = user_agent, auth=('user', 'pass'))
		d = r.text
		soup = BeautifulSoup(d, "html.parser")
		#page 수 찾기
		for end in soup.find_all('a', href=True):
			pass
		page = re.findall('\d+', end['href'][-4:])[0]


		for p in range(1, int(page)+1):
			url = "http://finance.naver.com/item/sise_day.nhn?code="+ticker[t] + "&page=" + str(p)
			df = pd.read_html(url, thousands='')

			#1999년인지 확인
			date_1999 = False

			if (p==int(page)):
				for i in range(1, len(df[0])):
					if(str(df[0].ix[i][0]) == "nan"):
						break
					date = df[0].ix[i][0].replace(".", "")
					if(date[0:4] == '1999'):
						date_1999 = True
						break
					open_price = int(df[0].ix[i][3].replace(",", ""))
					high_price = int(df[0].ix[i][4].replace(",", ""))
					low_price = int(df[0].ix[i][5].replace(",", ""))
					close_price = int(df[0].ix[i][1].replace(",", ""))
					volume = int(df[0].ix[i][6].replace(",", ""))
					code = Ticker.objects.filter(code=ticker[t]).first()
					#db에 저장
					data = OHLCV(code=code, date=date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price, volume=volume)
					data.save()

			else:
				for i in range(1,11):
					if(str(df[0].ix[i][0]) == "nan"):
						continue
					date = df[0].ix[i][0].replace(".", "")
					if(date[0:4] == '1999'):
						date_1999 = True
						break
					open_price = int(df[0].ix[i][3].replace(",", ""))
					high_price = int(df[0].ix[i][4].replace(",", ""))
					low_price = int(df[0].ix[i][5].replace(",", ""))
					close_price = int(df[0].ix[i][1].replace(",", ""))
					volume = int(df[0].ix[i][6].replace(",", ""))
					code = Ticker.objects.filter(code=ticker[t]).first()
					#db에 저장
					data = OHLCV(code=code, date=date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price, volume=volume)
					data.save()
			if(date_1999):
				break

		end_time = time.time()

		av_time = (av_time+(end_time-start_time))/2.0

		print(str(t)+" company took..", end_time-start_time)
		print("average = ", av_time)

f.close()
