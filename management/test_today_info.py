
from management.common_function import end_point_check
from restapi.models import Ticker
from restapi.models import OHLCV
from restapi.models import Info
from datetime import datetime
from bs4 import BeautifulSoup
import requests

#오늘의 날짜 
today_date = "20171211" #datetime.now().strftime("%Y%m%d")


# #모델 가져오기 
ticker = Ticker.objects.filter(date=today_date)
ohlcv = OHLCV.objects.filter(date=today_date)


#중단된 지점 확인 
index = end_point_check("data\\"+today_date+"_daily_info_log.txt", ticker)
index += 1 #다음 거부터 시작~

#log 기록용
f = open("data\\"+today_date+"_daily_info_log.txt", 'w')

for i in range(1, len(ticker)):
    url = "http://finance.naver.com/item/main.nhn?code="+ticker[i].code
    user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
    r = requests.get(url, headers= user_agent, auth=('user', 'pass'))
    d = r.text
    soup = BeautifulSoup(d, "html.parser")


    table = soup.find('div', {'class' : 'first'})
    #정보가 아예 없는 케이스도 있으려나? 있으면 빨리 발견됫으면...

    size_type = 'S' #tmp
    style_type = 'G' #tmp
        

    #액면가  
    face_val = table.find(text="액면가")
    if(face_val == None):
        #해당 정보가 없는 경우 
        face_val = 0
    else:
        face_val = int(face_val.find_next().find_next().find_next().string.replace(",", ""))

    #상장주식수
    stock_nums = table.find(text="상장주식수")
    if (stock_nums == None):
        stock_nums = 0
    else:
        stock_nums = int(stock_nums.find_next().string.replace(",", ""))

    # #시가총액
    close_price = ohlcv[i].close_price
    market_cap = close_price*stock_nums
    
    #시가총액 순위
    market_cap_rank = 0 #tmp
    
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

    f.write(str(i)+" "+ticker[i].code+"\n")


f.close()



# #industy
# index=0
# info_list = Info.objects.filter(date=today_date)
# #코스피 industry 저장 
# f = open("data\\20171206_kospi_industry.txt", 'r')
# for industry in f:
#     info_list[index].industry = industry[:-1] #\n 제거 
#     info_list[index].save()
#     index += 1
# f.close()

# kosdaq_start_index = index

# #코스닥 industry 저장
# f = open("data\\20171206_kosdaq_industry.txt", 'r')
# for industry in f:
#     info_list[index].industry = industry[:-1] #\n 제거 
#     info_list[index].save()
#     index += 1
# f.close()



# #시가총액 순위, 사이즈 
# orderd_info_list = Info.objects.order_by('-market_cap')
# for i in range(len(orderd_info_list)):
#     #시가 총액 순위 매기기
#     orderd_info = orderd_info_list[i]
#     orderd_info.market_cap_rank = (i+1)
    
#     if(i<kosdaq_start_index):
#         #코스피 사이즈 매기기 
#         if(i<100):
#             orderd_info.size_type = 'L'
#         elif(i<300):
#             orderd_info.size_type = 'M'
#     else:        
#         #코스닥 사이즈 매기기 
#         if (i-kosdaq_start_index <100):
#             orderd_info.size_type = 'L'
#         elif (i-kosdaq_start_index<400):
#             orderd_info.size_type = 'M'

#     #db에 반영 
#     orderd_info.save()






# #다시 코드 순서대로 정렬
# for i in range(len(Info.objects.filter(date=today_date))):
#   orderd_info = Info.objects.order_by('code')[i]
#   orderd_info.save()





# #데이터 삭제 
# for info in Info.objects.filter(date=today_date):
#     info.delete()

