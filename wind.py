import pandas as pd

def read_wind_excel(ticker, start, end):
    custom_col_converter = lambda x : float(x.replace('--','0'))
    df0 = pd.read_excel(ticker,
                        engine='openpyxl',
                        # encoding='GB2312',
                        parse_dates=['交易日期'],
                        thousands=',',
                        converters={'开盘点位':  custom_col_converter,
                                    "最高点位":  custom_col_converter,
                                    "最低点位":  custom_col_converter,
                                    "收盘价":    custom_col_converter,
                                    "成交量(万股)":custom_col_converter,
                                    },
                        index_col=0,
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
    df0.rename_axis('date',inplace=True)
    df0.sort_index(inplace=True)
    df0[start:end]

    return df0[start:end]