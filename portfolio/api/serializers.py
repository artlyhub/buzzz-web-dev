import time, datetime
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from portfolio.algorithms import PortfolioAlgorithm
from portfolio.models import Portfolio, PortfolioHistory
from restapi.models import OHLCV

User = get_user_model()


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('id',
                  'user',
                  'name',
                  'capital',
                  'portfolio_type',
                  'description',
                  'created',
                  'updated',)


class PortfolioHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioHistory
        fields = ('id',
                  'portfolio',
                  'date',
                  'code',
                  'status',
                  'quantity',
                  'price',)


class PortfolioDiagnosisSerializer(serializers.ModelSerializer):
    stock_num = serializers.SerializerMethodField()
    port_info = serializers.SerializerMethodField()
    close_price = serializers.SerializerMethodField()

    class Meta:
        model = Portfolio
        fields = ('id',
                  'user',
                  'name',
                  'capital',
                  'portfolio_type',
                  'description',
                  'stock_num',
                  'port_info',
                  'close_price',
                  'created',
                  'updated',)

    def get_stock_num(self, obj):
        return obj.history.count()

    def get_port_info(self, obj):
        # STEP 1: Calculate portfolio ratio
        stocks = obj.history.all()
        stock_counts = stocks.count()
        capital = obj.capital
        capital_per_stock = capital//stock_counts
        left_over_capital = 0
        ratio_dict = dict()
        ratio_dict['status'] = '동일 비중 포트폴리오'
        ratio_dict['ratio'] = dict()
        ohlcv_inst_list = list()
        for stock in stocks:
            code = stock.code.code
            ohlcv = OHLCV.objects.filter(code=stock.code)
            # exception handling for when our database isn't fully functional yet
            if ohlcv.exists():
                ohlcv_inst = ohlcv.order_by('-date').first()
                ohlcv_inst_list.append(ohlcv_inst)
                name = ohlcv_inst.code.name
                date = ohlcv_inst.date
                close_price = ohlcv_inst.close_price
                ratio_dict['ratio'][code] = dict()
                ratio_dict['ratio'][code]['name'] = name
                ratio_dict['ratio'][code]['date'] = date
                ratio_dict['ratio'][code]['price'] = close_price
                if close_price < capital_per_stock:
                    stock_num = capital_per_stock//close_price
                    invested = stock_num*close_price
                    ratio_dict['ratio'][code]['invested'] = invested
                    left_over_capital += capital_per_stock - invested
                    ratio_dict['ratio'][code]['buy_num'] = stock_num
            else:
                continue
        ratio_dict['ratio']['cash'] = left_over_capital
        redistribute = left_over_capital > 0
        while redistribute:
            extra_buy = list(filter(lambda x: x.close_price < left_over_capital, ohlcv_inst_list))
            if len(extra_buy) == 0:
                redistribute = False
                continue
            extra_capital_per_stock = left_over_capital//len(extra_buy)
            extra_buy_num = list(map(lambda x: extra_capital_per_stock//x.close_price, extra_buy))
            close_price_list = [ohlcv.close_price for ohlcv in extra_buy]
            reset_left_over = left_over_capital - sum(map(lambda x, y: x*y, extra_buy_num, close_price_list))
            extra_stocks = [ohlcv.code.code for ohlcv in extra_buy]
            for i in range(len(extra_stocks)):
                extra_invested = extra_buy_num[i]*close_price_list[i]
                ratio_dict['ratio'][extra_stocks[i]]['invested'] += extra_invested
                ratio_dict['ratio'][extra_stocks[i]]['buy_num'] += extra_buy_num[i]
            ratio_dict['ratio']['cash'] = reset_left_over
            ohlcv_inst_list = extra_buy
            left_over_capital = reset_left_over
        port_ratio = dict()
        for key, val in ratio_dict['ratio'].items():
            if key != 'cash':
                stock_ratio = val['invested']/capital
                ratio_dict['ratio'][key]['ratio'] = stock_ratio
        # STEP 2: Calculate portfolio specs
        pa = PortfolioAlgorithm(ratio_dict['ratio'])
        pa.create_ohlcv_df()
        r, v, sr, yield_r, bt = pa.portfolio_info()
        new_bt = pa.change_bt_format(bt)
        print(r)
        print(v)
        print(sr)
        print(yield_r)
        print(new_bt)
        return ratio_dict

    def get_close_price(self, obj):
        stocks = obj.history.all()
        # filter close price data to dates greater than filter_date
        price_dict = dict()
        last_year = str(datetime.datetime.now().year - 1)
        month = str(datetime.datetime.now().month).zfill(2)
        filter_date = last_year + month + '00'
        for stock in stocks:
            code = stock.code.code
            ohlcv = OHLCV.objects.filter(code=stock.code).distinct('date')
            ohlcv_w_filters = ohlcv.order_by('date').exclude(date__lte=filter_date)
            price_dict[code] = ohlcv_w_filters.values_list('date', 'close_price')
        return price_dict
