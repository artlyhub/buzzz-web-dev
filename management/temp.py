# import pickle
import os, sys, io
import pandas as pd
import requests
from bs4 import BeautifulSoup
from restapi.models import Ticker
from restapi.models import OHLCV


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://finance.naver.com/item/sise_day.nhn?code=032280"
print(url)
df = pd.read_html(url, thousands='')
market_date = df[0].ix[1][0]
print(type(market_date))
market_date = market_date.replace(".", "")
print(market_date)
print(market_date == "20171220")

#
#
#
#
# url = "http://finance.naver.com/item/coinfo.nhn?code=005930"
# user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
# r = requests.get(url, headers= user_agent, auth=('user', 'pass'))
# d = r.text
# soup = BeautifulSoup(d, "html.parser")
#
#
# # table = soup.find('div', {'class' : 'first'})
# industry = soup.find('div', {'id':'pArea'})#.find_next().find_next().find_next()
#
# print(industry)
# # print(table)














# with open('../sensitives.pickle', 'rb') as f:
# 	data = pickle.load(f)
# 	print(data)

# f.close()
# print(data['IP_ADDRESS'])

# data['IP_ADDRESS'] = '45.32.249.71'
# # data['IP_ADDRESS'] = '45.32.63.193'
# data['DEBUG'] = False
# pickle.dump(data, open("../sensitives.pickle", "wb"))


#아...중복된 데이터 지우는 건 일단 나중에..뀨..ㅠㅠ

# buzzz_url = 'http://buzzz.co.kr/api/ticker/'
# dest_path = os.getcwd() + '\\data'
# ticker = get_buzz_data("tmp_ticker", buzzz_url, dest_path)

# print(ticker['id'][0])

# index=3
# for t in range(650, 660):
# 	ohlcv = OHLCV.objects.filter(code=ticker['id'][t]).distinct('date')
# 	print("ohlcv: ", ohlcv)


# ex = OHLCV.objects.exclude(date__in=ohlcv.values('date'))
# print("ex: " , ex)


# d = ohlcv.values(code, date).order_by('code').distinct()
# print(d)
# ex = OHLCV.objects.exclude(date__in=d.values('date', flat=True))
# print (ex)

# Address.objects.exclude(pk__in=d.values('pk', flat=True)).delete()




# if not(OHLCV.objects.filter(date="20171208").filter(code=ticker[index]).exists): #.filter(code=ticker[3].id))
# 	print("not exists")
# else:
# 	print("exist!")
