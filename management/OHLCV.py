

from management.common_function import *

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


##setting
#오늘의 날짜
today_date = "20171211" #datetime.now().strftime("%Y%m%d")
#평균 걸린 시간
av_time = 0

print(os.getcwd())



#Ticker 가져오기(code)
# buzzz_url = 'http://buzzz.co.kr/api/ticker/'
dest_path = 'data'
# ticker = get_buzz_data(today_date+"_ticker", buzzz_url, dest_path)
ticker = Ticker.objects.filter(date="20171208")




#시작할 지점 찾기 
index = end_point_check(dest_path+"\\OHLCV_log.txt", ticker)
#중단된 회사 ohlcv 삭제 
print(OHLCV.objects.filter(code=ticker[index]))
OHLCV.objects.filter(code=ticker[index]).delete() 



#log파일 열기 
f = open(dest_path+"\\OHLCV_log.txt", 'w')

#OHLCV 
for t in range(index, 401):
	start_time = time.time()
	#log 기록(회사 code)
	f.write(str(t)+" "+ticker[t].code+"\n")

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
				elif (int(date[0:8])>int(today_date)): #지정 날짜 부터 저장하기 
					continue
				else:
					open_price = int(df[0].ix[i][3].replace(",", ""))
					high_price = int(df[0].ix[i][4].replace(",", ""))
					low_price = int(df[0].ix[i][5].replace(",", ""))
					close_price = int(df[0].ix[i][1].replace(",", ""))
					volume = int(df[0].ix[i][6].replace(",", ""))
					#code = Ticker.objects.filter(id=ticker['id'][t]).first()
					#db에 저장
					data = OHLCV(code=ticker[t], date=date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price, volume=volume)
					data.save()

		else:
			for i in range(1,11):
				if(str(df[0].ix[i][0]) == "nan"):
					continue
				date = df[0].ix[i][0].replace(".", "")
				if(date[0:4] == '1999'):
					date_1999 = True
					break
				elif (int(date[0:8])>int(today_date)): #지정 날짜 부터 저장하기 
					continue
				else:
					open_price = int(df[0].ix[i][3].replace(",", ""))
					high_price = int(df[0].ix[i][4].replace(",", ""))
					low_price = int(df[0].ix[i][5].replace(",", ""))
					close_price = int(df[0].ix[i][1].replace(",", ""))
					volume = int(df[0].ix[i][6].replace(",", ""))
					# code = Ticker.objects.filter(id=ticker['id'][t]).first()
					#db에 저장
					data = OHLCV(code=ticker[t], date=date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price, volume=volume)
					data.save()
		if(date_1999):
			break



	end_time = time.time()

	av_time = (av_time+(end_time-start_time))/2.0

	print(str(t)+" comany took..", end_time-start_time)
	print("average = ", av_time)

f.close()















