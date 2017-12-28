
from management.common_function import end_point_check
from restapi.models import Ticker
from restapi.models import OHLCV
from restapi.models import Info
from datetime import datetime
from bs4 import BeautifulSoup
import requests

import sys, io
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')




#오늘의 날짜
today_date = datetime.now().strftime("%Y%m%d")


# #모델 가져오기
ticker = Ticker.objects.filter(date=today_date)
ohlcv = OHLCV.objects.filter(date=today_date)


#중단된 지점 확인
index = end_point_check("data\\"+today_date+"_daily_info_log.txt", ticker)
index += 1 #다음 거부터 시작~


#log 기록용
f = open("data\\"+today_date+"_daily_info_log.txt", 'w')
info_list = []
for i in range(len(ticker)):
    url = "http://finance.naver.com/item/main.nhn?code="+ticker[i].code
    print(url)
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
        face_val = None
    else:
        face_val = float(face_val.find_next().find_next().find_next().string.replace(",", ""))
        if (10-face_val >10):
            face_val = None #USD인 경우
        else:
            face_val = int(face_val)



    #상장주식수
    stock_nums = table.find(text="상장주식수")
    if (stock_nums == None):
        stock_nums = None
    else:
        stock_nums = int(stock_nums.find_next().string.replace(",", ""))

    # #시가총액
    close_price = ohlcv[i].close_price
    market_cap = close_price*stock_nums

    #시가총액 순위
    market_cap_rank = None #tmp

    #industry
    url = "http://companyinfo.stock.naver.com/v1/company/c1010001.aspx?cmp_cd="+ticker[i].code
    user_agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
    r = requests.get(url, headers= user_agent, auth=('user', 'pass'))
    d = r.text
    soup = BeautifulSoup(d, "html.parser")
    tmp = soup.find('td', {'class' : 'cmp-table-cell td0101'})
    tmp = tmp.find_all('dt', {'class' : 'line-left'})

    industry = tmp[1].string.split(' : ')[1]


    #PER
    per = soup.find('em', {'id' : 'krx_per'})
    if (per is None):
        per = None
    else:
        per = float(per.string.replace(",", ""))
    #PBR
    pbr = soup.find('em', {'id' : '_pbr'})
    if (pbr is None):
        pbr = None
    else:
        pbr = float(pbr.string.replace(",", ""))
    #배당수익률
    yield_ret = soup.find('em', {'id' : '_dvr'})
    if (yield_ret is None):
        yield_ret = None
    else:
        yield_ret = float(yield_ret.string.replace(",", ""))


    #list에 info 저장
    data = Info(code=ticker[i].code, date=today_date, size_type=size_type, style_type=style_type,
                face_val=face_val, stock_nums=stock_nums, market_cap=market_cap, market_cap_rank=market_cap_rank,
                industry=industry, per=per, pbr=pbr, yield_ret=yield_ret)
    info_list.append(data)
    print('added ' + ticker[i].code + ' data')
    f.write(str(i)+" "+ticker[i].code+"\n")
#db에 저장
Info.objects.bulk_create(info_list)
print('saved to db')
#파일닫기
f.close()







#시가총액 순위, 사이즈
ordered_info_list = Info.objects.filter(date=today_date).order_by('-market_cap')
kospi_rank = 1
kosdaq_rank = 1
for ordered_info in ordered_info_list:
    if(ticker.filter(code=ordered_info.code)[0].market_type == "KP"): #코스피
        #시가총액 순위
        ordered_info.market_cap_rank = kospi_rank
        #코스피 사이즈 매기기
        if(kospi_rank<=100):
            ordered_info.size_type = 'L'
        elif(kospi_rank<=300):
            ordered_info.size_type = 'M'
        kospi_rank += 1
    else: #코스닥
        ordered_info.market_cap_rank = kosdaq_rank
        if (kosdaq_rank<=100):
            ordered_info.size_type = 'L'
        elif (kosdaq_rank<=400):
            ordered_info.size_type = 'M'
        kosdaq_rank += 1

    #db에 반영
    ordered_info.save()









# #데이터 삭제
# for info in Info.objects.filter(date=today_date):
#     info.delete()
