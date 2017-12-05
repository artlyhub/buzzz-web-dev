

#새로 생기는 종목들만 들고와서 추가하는 것도 고려해야해!!
#전날 종목이랑 비교해서 새로 추가된 종목만 OHLCV 실행하려면...
#따로 OHLCV_update.py 만들어서 하는게 낫겟땅
#어차피 OHLCV는 한번 돌리고 그 뒤론 계속 저거만 돌릴거아냥 




from datetime import datetime
from restapi.models import Ticker
from restapi.models import OHLCV
import pandas as pd
from bs4 import BeautifulSoup
import requests
import lxml
import re
import time


#오늘의 날짜
today_date = datetime.now().strftime("%Y%m%d")

#Ticker 가져오기(code)
ticker = Ticker.objects.filter(date=today_date)



#OHLCV 
for t in range(len(ticker)):
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
	time.sleep(0.5)



