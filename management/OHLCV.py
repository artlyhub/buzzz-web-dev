

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


#Ticker 가져오기(code)
buzzz_url = 'http://buzzz.co.kr/api/ticker/'
dest_path = os.getcwd() + '\\tests'

def get_buzzz_data(buzzz_url):
    r = requests.get(buzzz_url)
    if r.status_code == 200:
        data = r.json()
        df = pd.DataFrame(data['results'])
        prev_url = data['previous']
        next_url = data['next']
        print(buzzz_url)
    return df, prev_url, next_url

df, prev_url, next_url = get_buzzz_data(buzzz_url)
while next_url != None:
    buzzz_url = next_url
    temp_df, prev_url, next_url = get_buzzz_data(buzzz_url)
    df = df.append(temp_df, ignore_index=True)
df.to_csv(dest_path + '\\{}.csv'.format('ticker'), index=False)

ticker = df





# #중단된 지점 확인
# if (os.path.isfile("OHLCV_log.txt")):
# 	f = open("OHLCV_log.txt", 'r')
# 	#마지막 줄 회사 code만 읽어오기 
# 	for line in f:
# 		pass
# 	last_company = line
# 	f.close()

# 	while not(ticker[index].code+"\n" == last_company):
# 		index += 1
# 	#중단된 회사 ohlcv 삭제 
# 	OHLCV.objects.filter(code=ticker[index]).delete() 






#코스닥
#필터링 귀차..ㄴ..
index = 775

#log파일 열기 
f = open("OHLCV_log.txt", 'w')

#OHLCV 
for t in range(index, len(ticker)):
	start_time = time.time()
	#log 기록(회사 code)
	f.write(ticker['code'][t]+"\n")

	#사이트 html 가져오기
	url = "http://finance.naver.com/item/sise_day.nhn?code="+ticker['code'][t]
	user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
	r = requests.get(url, headers = user_agent, auth=('user', 'pass'))
	d = r.text
	soup = BeautifulSoup(d, "html.parser")
	#page 수 찾기 
	for end in soup.find_all('a', href=True):
		pass
	page = re.findall('\d+', end['href'][-4:])[0]


	for p in range(1, int(page)+1):
		url = "http://finance.naver.com/item/sise_day.nhn?code="+ticker['code'][t] + "&page=" + str(p) 
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
				code = Ticker.objects.filter(id=ticker['id'][t]).first()
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
				code = Ticker.objects.filter(id=ticker['id'][t]).first()
				#db에 저장
				data = OHLCV(code=code, date=date, open_price=open_price, high_price=high_price, low_price=low_price, close_price=close_price, volume=volume)
				data.save()
		if(date_1999):
			break



	end_time = time.time()

	av_time = (av_time+(end_time-start_time))/2.0

	print(str(t)+" comany took..", end_time-start_time)
	print("average = ", av_time)

f.close()















