# import pickle
import os
import pandas as pd
from restapi.models import Ticker
from restapi.models import OHLCV
# from management.common_function import *

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
 



# ticker = Ticker.objects.filter(date="20171208").filter(code="027740")
# print(ticker)
# print(ticker[0])
# print(len(ticker))
# print(ticker[3].code)
# print(ticker[3].name)



# if not(OHLCV.objects.filter(date="20171208").filter(code=ticker[index]).exists): #.filter(code=ticker[3].id))
# 	print("not exists")
# else:
# 	print("exist!")


# for i in range(10):
# 	print(ohlcv[i])
# 	print(ohlcv[i].code)
# 	print(ohlcv[i].date)

# if not(OHLCV.objects.filter(code=ticker[3].id).filter(date="20171208").exists()):
# 	print("2")
# else:
# 	print("3")

#빈파일 여부 확인
# print(os.stat("..\\data\\OHLCV_log.txt").st_size == 0)

# ticker = Ticker.objects.filter(date="20171208")

# for i in range(8):
# 	ohlcv = OHLCV.objects.filter(code=ticker[i])
# 	print(ohlcv)
# 	print(len(ohlcv))
	# for j in range(len(ohlcv)):
	# 	if(j>=int(len(ohlcv)/2)):
	# 		ohlcv[j].delete()


ticker = Ticker.objects.filter(date="20171211")
print(ticker[124].code)
print(ticker[125].code)
print(ticker[126].code)
# for i in range(774):
# 	print(str(i)+" ", OHLCV.objects.filter(code=ticker[i]))
# 	print(len(OHLCV.objects.filter(code=ticker[i])))

