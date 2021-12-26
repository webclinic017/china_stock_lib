import pandas as pd
import backtrader as bt


def read_wind_excel(ticker, start, end, skiprows, header):
    custom_col_converter = lambda x: float(x.replace('--', '0'))
    df0 = pd.read_excel(ticker,
                        engine='openpyxl',
                        # encoding='GB2312',
                        parse_dates=['交易日期'],
                        thousands=',',
                        converters={'开盘点位': custom_col_converter,
                                    "最高点位": custom_col_converter,
                                    "最低点位": custom_col_converter,
                                    "收盘价": custom_col_converter,
                                    "成交量(万股)": custom_col_converter,
                                    },
                        index_col=0,
                        skiprows=skiprows,
                        header=header,
                        ) \
        .rename(
        columns={
            "交易日期": "datetime",
            "开盘点位": "open",
            "最高点位": "high",
            "最低点位": "low",
            "收盘价": "close",
            "成交量(万股)": "volume",
        },
    )
    df0.rename_axis('date', inplace=True)
    df0.sort_index(inplace=True)
    df0[start:end]

    return df0[start:end]


class PandasDataFeed(bt.feeds.PandasDirectData):
    params = (
        ('dtformat', '%Y-%m-%d'),
        ('datetime', 0),
        ('open', 1),
        ('high', 2),
        ('low', 3),
        ('close', 4),
        ('volume', 9),
        ('openinterest', -1),
    )
