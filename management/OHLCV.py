

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
work_time = []
av_time = 0


index = 0


#Ticker 가져오기(code)
ticker = Ticker.objects.filter(date=today_date)



#중단된 지점 확인
if (os.path.isfile("OHLCV_log.txt")):
	f = open("OHLCV_log.txt", 'r')
	#마지막 줄 회사 code만 읽어오기 
	for line in f:
		pass
	last_company = line
	f.close()

	while not(OHLCV.objects.filter(code=ticker[index].code) == last_company):
		index += 1
	index += 1 #중단된 지점 
	#중단된 회사 ohlcv 삭제 
	OHLCV.objects.filter(code=ticker[index].code).delete() 



#log파일 열기 
f = open("OHLCV_log.txt", 'w')

#OHLCV 
for t in range(index, len(ticker)+1):
	start_time = time.time()
	#log 기록(회사 code)
	f.write(ticker[k].code+"\n")

	#사이트 html 가져오기
	url = "http://finance.naver.com/item/sise_day.nhn?code="+ticker[t].code
	user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
	r = requests.get(url, headers = user_agent, auth=('user', 'pass'))
	d = r.text
	soup = BeautifulSoup(d, "html.parser")
	#page 수 찾기 
	for end in soup.find_all('a', href=True):
		pass
	page = re.findall('\d+', end['href'][-4:])[0]


	for p in range(1, int(page)+1):
		url = "http://finance.naver.com/item/sise_day.nhn?code="+ticker[t].code + "&page=" + str(p) 
		df = pd.read_html(url, thousands='')
		if (p==int(page)):
			for i in range(1, len(df[0])):
				if(str(df[0].ix[i][0]) == "nan"):
					break
				date = df[0].ix[i][0].replace(".", "")
				open_price = int(df[0].ix[i][3].replace(",", ""))
				high_price = int(df[0].ix[i][4].replace(",", ""))
				low_price = int(df[0].ix[i][5].replace(",", ""))
				close_price = int(df[0].ix[i][1].replace(",", ""))
				volume = int(df[0].ix[i][6].replace(",", ""))
				#db에 저장
				data = OHLCV(code=ticker[t], date=date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price, volume=volume)
				data.save()

		else:
			for i in range(1,11):
				date = df[0].ix[i][0].replace(".", "")
				open_price = int(df[0].ix[i][3].replace(",", ""))
				high_price = int(df[0].ix[i][4].replace(",", ""))
				low_price = int(df[0].ix[i][5].replace(",", ""))
				close_price = int(df[0].ix[i][1].replace(",", ""))
				volume = int(df[0].ix[i][6].replace(",", ""))
				#db에 저장
				data = OHLCV(code=ticker[t], date=date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price, volume=volume)
				data.save()
	
	end_time = time.time()
	time.sleep(0.5)

	work_time.append(end_time-start_time)
	av_time = (av_time+(end_time-start_time))/2.0

	print("this comany took..", end_time-start_time)
	print("average = ", av_time)
f.close()




