
from restapi.models import Ticker
from restapi.models import OHLCV
from datetime import datetime
import pandas as pd
from bs4 import BeautifulSoup
import requests
# import simplejson as json
# from celery.decorators import task
import time

#일단 db가 안지워지니까...이거 걸리는 시간은 내일 확인해야겠다...ㅋ 
def get_ohlcv():
	start_time = time.time()
	#오늘 날짜
	date = datetime.now().strftime('%Y%m%d')
	#ticker가져오기
	ticker = Ticker.objects.filter(date=date)

	for i in range(len(ticker)):
    #코드 별 당일 시세 사이트에서 가져오기
    url = "http://finance.naver.com/item/sise_day.nhn?code="+ticker[i].code
    user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
    r = requests.get(url, headers = user_agent, auth=('user', 'pass'))
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    if not(OHLCV.filter(code=ticker[i]).filter(date=date).exists()):
    	#오늘 날짜 
	    day = soup.find('span', {'class' : 'tah p10 gray03'}).string
	    #ohlcv
	    close_price = day.find_next().string
	    tmp = closingPrice.find_next().find_next().find_next()
	    open_price = tmp.find_next().string
	    high_price = marketPrice.find_next().string
	    low_price = highPrice.find_next().string
	    volume = lowPrice.find_next().string
	    #db에 저장
	    data = OHLCV(code=ticker[i], date=date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price, volume=volume)
 		data.save()


	
# 	for i in range(len(ticker)):
# 		if not(OHLCV.objects.filter(code=ticker[i]).filter(date=date).exists()):
# 			#OHLCV
# 			url = "http://finance.naver.com/item/sise_day.nhn?code="+str(ticker[i].code) 
# 			df = pd.read_html(url, thousands='')
			
# 			open_price = int(df[0].ix[1][3].replace(",", ""))
# 			high_price = int(df[0].ix[1][4].replace(",", ""))
# 			low_price = int(df[0].ix[1][5].replace(",", ""))
# 			close_price = int(df[0].ix[1][1].replace(",", ""))
# 			volume = int(df[0].ix[1][6].replace(",", ""))

# 			data = OHLCV(code=ticker[i], date=date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price, volume=volume)
# 			data.save()

# 	end_time = time.time()
# 	print(end_time-start_time)

 get_ohlcv()






    
    
