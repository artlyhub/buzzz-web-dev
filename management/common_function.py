# from restapi.models import OHLCV
from bs4 import BeautifulSoup
import pandas as pd
import requests
import lxml
import os



# #한 페이지의 데이터 긁어오기 
# def buzzz_data(buzzz_url):
#     r = requests.get(buzzz_url)
#     if r.status_code == 200:
#         data = r.json()
#         df = pd.DataFrame(data['results'])
#         prev_url = data['previous']
#         next_url = data['next']
#         print(buzzz_url)
#     return df, prev_url, next_url



# def get_buzz_data(data_file_name, buzzz_url, dest_path):
# 	df, prev_url, next_url = buzzz_data(buzzz_url)
# 	while next_url != None:
# 	    buzzz_url = next_url
# 	    temp_df, prev_url, next_url = buzzz_data(buzzz_url)
# 	    df = df.append(temp_df, ignore_index=True)
# 	df.to_csv(dest_path + '\\{}.csv'.format(data_file_name), index=False)
# 	return df




#중단된 지점 확인(ohlcv, info crawler)
def end_point_check(log_file_name, ticker):
	index = 0
	if (os.path.isfile(log_file_name) and not (os.stat(log_file_name).st_size == 0)):
		f = open(log_file_name, 'r')
		#마지막 줄 회사 code만 읽어오기 
		for line in f:
			pass
		last_company = line
		print(last_company)
		f.close()
		while not(ticker[index].code == last_company[-7:-1]):
			index += 1
			print(index)
		return index
	else:
		return index #0



