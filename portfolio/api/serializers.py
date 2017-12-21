import time, datetime
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from portfolio.algorithms import PortfolioAlgorithm
from portfolio.models import Portfolio, PortfolioHistory
from restapi.models import Ticker, OHLCV, Specs

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
    port_specs = serializers.SerializerMethodField()

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
                  'port_specs',
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
        ohlcv_inst_list = list()
        for stock in stocks:
            code = stock.code.code
            ohlcv = OHLCV.objects.filter(code=stock.code.code)
            # exception handling for when our database isn't fully functional yet
            if ohlcv.exists():
                ohlcv_inst = ohlcv.order_by('-date').first()
                ohlcv_inst_list.append(ohlcv_inst)
                ticker_inst = Ticker.objects.filter(code=ohlcv_inst.code).order_by('-date').first()
                name = ticker_inst.name
                date = ohlcv_inst.date
                close_price = ohlcv_inst.close_price
                stock_data = {
                    'name': name,
                    'date': date,
                    'price': int(close_price)
                }
                ratio_dict[code] = stock_data
                if close_price < capital_per_stock:
                    stock_num = capital_per_stock//close_price
                    invested = stock_num*close_price
                    ratio_dict[code]['invested'] = int(invested)
                    left_over_capital += capital_per_stock - invested
                    ratio_dict[code]['buy_num'] = int(stock_num)
                else:
                    ratio_dict[code]['invested'] = 0
                    ratio_dict[code]['buy_num'] = 0
            else:
                continue
        ratio_dict['cash'] = left_over_capital
        redistribute = left_over_capital > 0
        while redistribute:
            extra_buy = list(filter(lambda x: x.close_price < left_over_capital, ohlcv_inst_list))
            if len(extra_buy) == 0:
                redistribute = False
                continue
            extra_capital_per_stock = left_over_capital//len(extra_buy)
            extra_buy_num = list(map(lambda x: extra_capital_per_stock//x.close_price, extra_buy))
            if sum(extra_buy_num) == 0:
                redistribute = False
                continue
            close_price_list = [ohlcv.close_price for ohlcv in extra_buy]
            reset_left_over = int(left_over_capital - sum(map(lambda x, y: x*y, extra_buy_num, close_price_list)))
            extra_stocks = [ohlcv.code for ohlcv in extra_buy]
            for i in range(len(extra_stocks)):
                extra_invested = extra_buy_num[i]*close_price_list[i]
                ratio_dict[extra_stocks[i]]['invested'] += int(extra_invested)
                ratio_dict[extra_stocks[i]]['buy_num'] += int(extra_buy_num[i])
            ratio_dict['cash'] = reset_left_over
            ohlcv_inst_list = extra_buy
            left_over_capital = reset_left_over
        for key, val in ratio_dict.items():
            if key != 'cash':
                stock_ratio = val['invested']/capital
                ratio_dict[key]['ratio'] = round(stock_ratio, 4)
        # STEP 2: Calculate portfolio specs
        port_info = {'status': '동일 비중 포트폴리오', 'ratio': ratio_dict}
        pa = PortfolioAlgorithm(ratio_dict)
        r, v, sr, yield_r, bt = pa.portfolio_info()
        new_bt = pa.change_bt_format(bt)
        port_info['return'] = round(yield_r, 3)*100
        port_info['average_return'] = round(r, 3)*100
        port_info['average_volatility'] = round(v, 3)*100
        port_info['sharpe_ratio'] = round(sr, 3)
        port_info['backtest_result'] = new_bt
        return port_info

    def get_port_specs(self, obj):
        stocks = obj.history.all()
        stock_counts = stocks.count()
        mom_s = 0
        volt_s = 0
        cor_s = 0
        vol_s = 0
        tot_s = 0
        for stock in stocks:
            code = stock.code.code
            specs = Specs.objects.filter(code=stock.code.code).order_by('date').first()
            mom_s += specs.momentum_score
            volt_s += specs.volatility_score
            cor_s += specs.correlation_score
            vol_s += specs.volume_score
            tot_s += (specs.momentum_score + specs.volatility_score + specs.correlation_score + specs.volume_score)/4
        mom_s = mom_s//stock_counts
        volt_s = volt_s//stock_counts
        cor_s = cor_s//stock_counts
        vol_s = vol_s//stock_counts
        tot_s = int(tot_s//stock_counts)
        return [tot_s, mom_s, volt_s, cor_s, vol_s]
