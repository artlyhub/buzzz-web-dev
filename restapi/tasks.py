
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


@task(name="scrape_naver_info")
def getInfo():
	#오늘의 날짜 
	today_date = datetime.now().strftime("%Y%m%d")

	#모델 가져오기 
	ticker = Ticker.objects.filter(date=today_date)
	ohlcv = OHLCV.objects.filter(date=today_date)


	for i in range(len(ticker)):
	    url = "http://finance.naver.com/item/main.nhn?code="+ticker[i].code
	    user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
	    r = requests.get(url, headers= user_agent, auth=('user', 'pass'))
	    d = r.text
	    soup = BeautifulSoup(d, "html.parser")


	    table = soup.find('div', {'class' : 'first'}).find_next().find_all('em')

	    size_type = 'S' #tmp
	    style_type = 'G' #tmp
	    face_val = int(table[3].string.replace(",", ""))
	    stock_nums = int(table[2].string.replace(",", ""))
	    # #시가총액
	    close_price = ohlcv[i].close_price
	    market_cap = close_price*stock_nums
	    #시가총액 순위
	    market_cap_rank = 0
	    #산업
	    industry = "NON" #tmp

	    #PER
	    per = soup.find('em', {'id' : 'krx_per'})
	    if (per is None):
	        per = 0
	    else:
	        per = float(per.string.replace(",", ""))
	    #PBR
	    pbr = soup.find('em', {'id' : '_pbr'})
	    if (pbr is None):
	        pbr = 0
	    else:
	        pbr = float(pbr.string.replace(",", ""))
	    #배당수익률
	    yield_ret = soup.find('em', {'id' : '_dvr'})
	    if (yield_ret is None):
	        yield_ret = 0
	    else:
	        yield_ret = float(yield_ret.string.replace(",", ""))


	    #db에 저장 
	    data = Info(code=ticker[i], date=today_date, size_type=size_type, style_type=style_type, 
	                face_val=face_val, stock_nums=stock_nums, market_cap=market_cap, market_cap_rank=market_cap_rank,
	                industry=industry, per=per, pbr=pbr, yield_ret=yield_ret)
	    data.save()




	#industy
	index=0
	info_list = Info.objects.filter(date=today_date)
	#코스피 industry 저장 
	f = open("data\\20171206_kospi_industry.txt", 'r')
	for industry in f:
	    info_list[index].industry = industry[:-1] #\n 제거 
	    info_list[index].save()
	    index += 1
	f.close()

	kosdaq_start_index = index

	#코스닥 industry 저장
	f = open("data\\20171206_kosdaq_industry.txt", 'r')
	for industry in f:
	    info_list[index].industry = industry[:-1] #\n 제거 
	    info_list[index].save()
	    index += 1
	f.close()



	#시가총액 순위, 사이즈 
	orderd_info_list = Info.objects.order_by('-market_cap')
	for i in range(len(orderd_info_list)):
	    #시가 총액 순위 매기기
	    orderd_info = orderd_info_list[i]
	    orderd_info.market_cap_rank = (i+1)
	    
	    if(i<kosdaq_start_index):
	        #코스피 사이즈 매기기 
	        if(i<100):
	            orderd_info.size_type = 'L'
	        elif(i<300):
	            orderd_info.size_type = 'M'
	    else:        
	        #코스닥 사이즈 매기기 
	        if (i-kosdaq_start_index <100):
	            orderd_info.size_type = 'L'
	        elif (i-kosdaq_start_index<400):
	            orderd_info.size_type = 'M'

	    #db에 반영 
	    orderd_info.save()






	#다시 코드 순서대로 정렬
	for i in range(len(Info.objects.filter(date=today_date))):
	  orderd_info = Info.objects.order_by('code')[i]
	  orderd_info.save()












