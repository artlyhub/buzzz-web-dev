import time
from restapi.models import OHLCV


ticker_list = ['005930', '000660', '005380', '005490', '035420', '051910',
               '105560', '012330', '015760', '032830', '068270', '091990',
               '130960', '263750', '086900', '003670', '034230', '036490',
               '253450', '046890', '151910']

# # method 1
# start_time = time.time()
# ohlcv_list = []
# for ticker in ticker_list:
#     ohlcv_qs = OHLCV.objects.filter(code=ticker).distinct('date')
#     ohlcv = list(ohlcv_qs.exclude(date__lte='20160100').values('date', 'close_price'))
#     ohlcv_list.append(ohlcv)
# print(ohlcv_list)
# end_time = time.time()
# print('time took: ', str(end_time - start_time))

# method 2
start_time = time.time()
ohlcv_qs = OHLCV.objects.filter(code__in=ticker_list)
ohlcv_qs = ohlcv_qs.exclude(date__lte='20160100').order_by('date')
ohlcv_qs = ohlcv_qs.values_list('code', 'date', 'close_price')
end_time = time.time()
print('time took: ', str(end_time - start_time))

start_time = time.time()
ohlcv_list = []
for ticker in ticker_list:
    ticker_ohlcv = [{'date': data[1], 'close_price': data[2]} for data in ohlcv_qs if data[0] == ticker]
    ohlcv_list.append(ticker_ohlcv)
end_time = time.time()
print('time took: ', str(end_time - start_time))

# start_time = time.time()
# ohlcv_list = [list(filter(lambda data: data['code'] == ticker, ohlcv_qs)) for ticker in ticker_list]
# end_time = time.time()
# print('time took: ', str(end_time - start_time))

for ohlcv in ohlcv_list[0]:
    print(ohlcv)
