import math, datetime
import numpy as np
import pandas as pd

from restapi.models import Ticker, OHLCV


class PortfolioAlgorithm:
    def __init__(self, ratio_dict, filter_date=False):
        self.ratio_dict = ratio_dict
        if not filter_date:
            last_year = str(datetime.datetime.now().year - 1)
            last_month = datetime.datetime.now().month - 1 or 12
            last_month = str(last_month).zfill(2)
            filter_date = last_year + last_month + '00'
            self.filter_date = filter_date
        else:
            self.filter_date = filter_date
        self.ohlcv_df = pd.DataFrame()
        self.settings = {
            'ticker_list': list(),
            'ohlcv_list': list()
        }
        self._start_df_setup() # fill in ticker_list and ohlcv_list
        self._retrieve_weights()
        self._create_ohlcv_df()
        self._calc_port_returns()

    def _start_df_setup(self):
        for key, val in self.ratio_dict.items():
            if key != 'cash':
                self.settings['ticker_list'].append(key)
                ohlcv_qs = OHLCV.objects.filter(code=key).distinct('date')
                ohlcv = list(ohlcv_qs.exclude(date__lte=self.filter_date).values('date', 'close_price'))
                self.settings['ohlcv_list'].append(ohlcv)

    def _retrieve_weights(self):
        S = list()
        W = list()
        for key, val in self.ratio_dict.items():
            if key != 'cash':
                S.append(key)
                W.append(val['ratio'])
        W = pd.Series(W, index=S)
        self.W = W

    def _create_ohlcv_df(self):
        ticker_count = len(self.settings['ticker_list'])
        if ticker_count == 0:
            pass
        elif ticker_count == 1:
            ticker = self.settings['ticker_list'][0]
            ohlcv = self.settings['ohlcv_list'][0]
            self.ohlcv_df = self._create_df(ticker, ohlcv)
        else:
            for i in range(ticker_count):
                ticker = self.settings['ticker_list'][i]
                ohlcv = self.settings['ohlcv_list'][i]
                if i == 0:
                    df = self._create_df(ticker, ohlcv)
                else:
                    temp_df = self._create_df(ticker, ohlcv)
                    df = pd.concat([df, temp_df], axis=1)
            df.index = pd.to_datetime(df.index)
            self.ohlcv_df = df

    def _create_df(self, ticker, ohlcv):
        df = pd.DataFrame(ohlcv)
        df.set_index('date', inplace=True)
        df.rename(columns={'close_price': ticker}, inplace=True)
        return df

    def _calc_port_returns(self, period='M'):
        self.ohlcv_df.index = pd.to_datetime(self.ohlcv_df.index)
        R = self.ohlcv_df.resample(period).last().pct_change()
        R.dropna(how='all', inplace=True)
        self.R = R

    def portfolio_info(self):
        BM_wr, BM_r, BM_v, BM_yc = self._bm_specs()
        wr, r, v, yc = self._backtest_port(self.W, self.R)
        sr = self._sharpe_ratio(r, BM_r, v)
        yield_r = yc.ix[len(yc)-1] - 1
        bt = pd.concat([yc, BM_yc], axis=1)
        bt.columns = ['Portfolio', 'Benchmark']
        return r, v, sr, yield_r, bt

    def _bm_specs(self, period='M'):
        BM_qs = OHLCV.objects.filter(code='BM').distinct('date')
        BM_data = list(BM_qs.exclude(date__lte=self.filter_date).values('date', 'close_price'))
        BM = pd.DataFrame(BM_data)
        BM.set_index('date', inplace=True)
        BM.index = pd.to_datetime(BM.index)
        BM.rename(columns={'close_price': 'Benchmark'}, inplace=True)
        BM_R = BM.resample(period).last().pct_change()
        BM_R.dropna(how='all', inplace=True)
        W = pd.Series([1], index=['Benchmark'])
        return self._backtest_port(W, BM_R)

    def _backtest_port(self, W=None, BM=None):
        if type(W) == type(None) and type(BM) == type(None):
            W_R = self.W * self.R
        else:
            W_R = W*BM
        WR = W_R.sum(axis=1)
        port_ret = WR.mean()
        port_var = WR.std()
        yield_curve = (WR + 1).cumprod()
        return WR, port_ret, port_var, yield_curve

    def _sharpe_ratio(self, r, bm_r, v):
        return (r - bm_r)/v

    def change_bt_format(self, bt):
        new_data = dict()
        for column in bt.columns:
            ret_data = list()
            # dates = bt.index.astype(np.int64)
            dates = bt.index
            for i in range(len(bt)):
                data = bt.ix[i]
                date = dates[i]
                ret_data.append([date, round(data[column], 4)])
            new_data[column] = ret_data
        return new_data


class BlackLitterman:
    def __init__(self):
        pass
