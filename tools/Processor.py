import pandas as pd
from datetime import datetime
import time

from restapi.models import Info, Ticker, OHLCV, Specs

DATA_PATH = 'C:/Users/hori9/Desktop/MINED/devcode/data'


class Processor(object):
    def __init__(self, filter_date=False):
        date = datetime.now().strftime('%Y%m%d')
        tickers = Ticker.objects.filter(date=date).values_list('code')
        # self.ticker_list = ['005930', '000660', '005380', '005490']
        self.ticker_list = [ticker[0] for ticker in list(tickers)]
        if not filter_date:
            last_year = str(datetime.now().year - 1)
            last_month = datetime.now().month - 1 or 12
            last_month = str(last_month).zfill(2)
            filter_date = last_year + last_month + '00'
            self.filter_date = filter_date

    def make_data(self):
        start = time.time()
        self.ohlcv_list = []
        self.volume_list = []
        init_qs = OHLCV.objects.filter(code__in=self.ticker_list)
        filtered_qs = init_qs.exclude(date__lte=self.filter_date).order_by('date')
        ohlcv_qs = filtered_qs.values_list('code', 'date', 'close_price', 'volume')
        self.price_list = []
        self.volume_list = []
        for ticker in self.ticker_list:
            ticker_price = [{'date': data[1], 'close_price': data[2]} for data in ohlcv_qs if data[0] == ticker]
            ticker_volume = [{'date': data[1], 'volume': data[3]} for data in ohlcv_qs if data[0] == ticker]
            self.price_list.append(ticker_price)
            self.volume_list.append(ticker_volume)
        end = time.time()
        print('time took: ', str(end-start))

        start = time.time()
        for i in range(len(self.ticker_list)):
            print(i)
            ticker = self.ticker_list[i]
            ohlcv = self.price_list[i]
            vol = self.volume_list[i]
            if i == 0:
                ohlcv_df = self._create_df(ticker, ohlcv, 'close_price')
                vol_df = self._create_df(ticker, vol, 'volume')
            else:
                temp_ohlcv_df = self._create_df(ticker, ohlcv, 'close_price')
                temp_vol_df = self._create_df(ticker, vol, 'volume')
                ohlcv_df = pd.concat([ohlcv_df, temp_ohlcv_df], axis=1)
                vol_df = pd.concat([vol_df, temp_vol_df], axis=1)
        ohlcv_df.index = pd.to_datetime(ohlcv_df.index)
        vol_df.index = pd.to_datetime(vol_df.index)
        self.ohlcv_df = ohlcv_df
        self.vol_df = vol_df
        self.ohlcv_df.to_csv(DATA_PATH + '/ohlcv_df.csv')
        self.vol_df.to_csv(DATA_PATH + '/vol_df.csv')
        end = time.time()
        print('time took: ', str(end-start))
        print('created csv files')

    def _create_df(self, ticker, ohlcv, col_name):
        df = pd.DataFrame(ohlcv)
        df.set_index('date', inplace=True)
        if col_name == 'close_price':
            df.rename(columns={col_name: ticker}, inplace=True)
        if col_name == 'volume':
            df.rename(columns={col_name: ticker}, inplace=True)
        return df

    def score_data(self):
        self._get_data_local()
        self.vol = (self.ohlcv_df * self.vol_df).ix[-1]
        self._set_return_portfolio()
        self._add_bm_data()
        self._save_mom_volt_cor_vol()

    def _get_data_local(self):
        self.ohlcv_df = pd.read_csv(DATA_PATH + '/ohlcv_df.csv', header=0, index_col='date', parse_dates=True)
        self.vol_df = pd.read_csv(DATA_PATH + '/vol_df.csv', header=0, index_col='date', parse_dates=True)

    def _set_return_portfolio(self):
        self.portfolio_data = self.ohlcv_df.pct_change()

    def _add_bm_data(self):
        BM_qs = OHLCV.objects.filter(code='BM')
        BM_data = list(BM_qs.exclude(date__lte=self.filter_date).values('date', 'close_price'))
        BM = pd.DataFrame(BM_data)
        BM.set_index('date', inplace=True)
        BM.index = pd.to_datetime(BM.index)
        BM.rename(columns={'close_price': 'Benchmark'}, inplace=True)
        BM = BM.pct_change()
        self.portfolio_data.index = pd.to_datetime(self.portfolio_data.index)
        self.portfolio_data = pd.concat([self.portfolio_data, BM], axis=1)
        self.portfolio_data.fillna(0, inplace=True)

    def _dual_momentum(self):
        # codes = list(close_data.columns)
        return_data = self.portfolio_data
        for i in range(1, 13):
            momentum = return_data - return_data.shift(i)
            if i == 1:
                temp = momentum
            else:
                temp += momentum
        mom = temp/12
        self.mom = mom.ix[-1]

    def _calc_volatility(self):
        self.volt = pd.DataFrame(self.portfolio_data).rolling(window=12).std().ix[-1]

    def _calc_correlation(self):
        self.cor = self.portfolio_data.corr()['Benchmark']

    def _save_mom_volt_cor_vol(self):
        self._dual_momentum()
        self._calc_volatility()
        self._calc_correlation()

        mom_s = self.mom.rank(ascending=True)
        mom_s = (mom_s/mom_s.max())*100
        volt_s = self.volt.rank(ascending=False)
        volt_s = (volt_s/volt_s.max())*100
        cor_s = self.cor.rank(ascending=False)
        cor_s = (cor_s/cor_s.max())*100
        vol_s = self.vol.rank(ascending=True)
        vol_s = (vol_s/vol_s.max())*100

        date = datetime.now().strftime('%Y%m%d')
        specs_list = []
        for ticker in self.ticker_list:
            momentum_score = mom_s[ticker]
            volatility_score = volt_s[ticker]
            correlation_score = cor_s[ticker]
            volume_score = vol_s[ticker]
            total_score = (momentum_score + volatility_score + correlation_score + volume_score)//4
            specs_inst = Specs(code=ticker,
                               date=date,
                               momentum=self.mom[ticker],
                               volatility=self.volt[ticker],
                               correlation=self.cor[ticker],
                               volume=self.vol[ticker],
                               momentum_score=momentum_score,
                               volatility_score=volatility_score,
                               correlation_score=correlation_score,
                               volume_score=volume_score,
                               total_score=total_score)
            specs_list.append(specs_inst)
            print('Added {} specs'.format(ticker))
        Specs.objects.bulk_create(specs_list)
