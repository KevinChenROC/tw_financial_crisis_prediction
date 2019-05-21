import os
from os.path import isfile, join

import pandas as pd
import numpy as np

from data_fetching import config
from data_transform.util.calc_rate_helper import *
from data_transform.util.lag_values_helper import *
from data_transform.util.file_extension import *


def get_file_names(dir_path):
    file_names = [f for f in os.listdir(
        dir_path) if isfile(join(dir_path, f))]
    return file_names


def get_lag_log_rates(series, lag_n, symbol, fill_freq):
    series = calc_log_rates(series)
    df = calc_lag_values(series, lag_n, symbol)

    # back fill missing values
    df = df.asfreq(freq=fill_freq, method='bfill')
    return df


def merge_time_series_datas(datas_path, value_col, lag_n, fill_freq='1D'):
    time_indexes = pd.date_range(config.START_DATE, config.END_DATE, freq='1D')
    target_df = pd.DataFrame(index=time_indexes)

    for f in get_file_names(datas_path):
        df = pd.read_csv(datas_path+f,
                         header=0, parse_dates=[0], index_col=0)

        # transform data
        df = get_lag_log_rates(
            df[value_col], lag_n, remove_extension(f), fill_freq)

        # merge dataframes
        target_df = target_df.join(df, how="inner")

    return target_df


stocks = merge_time_series_datas(
    datas_path=config.STOCK_INDX_PATH, value_col='Close', lag_n=config.STOCK_LAG_N)
