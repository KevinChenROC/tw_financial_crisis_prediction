import os
from os.path import isfile, join

import pandas as pd
import numpy as np

from data_fetching import config
from data_transform.util.calc_rate import *
from data_transform.util.lag_value import *
from data_transform.util.file_extension import *


def get_file_names(dir_path):
    file_names = [f for f in os.listdir(
        dir_path) if isfile(join(dir_path, f))]
    return file_names


def get_lag_change_rates(series, lag_n, symbol, fill_freq):
    series = calc_simple_rates(series)
    df = calc_lag_values(series, lag_n, symbol)

    # back fill missing values
    df = df.asfreq(freq=fill_freq, method='bfill')
    return df


# Merge different datas
def merge_data(data_dir, value_col, lag_n, fill_freq='1D'):
    time_indexes = pd.date_range(config.START_DATE, config.END_DATE, freq='1D')
    target_df = pd.DataFrame(index=time_indexes)

    for f in get_file_names(data_dir):
        df = pd.read_csv(data_dir+f,
                         header=0, parse_dates=[0], index_col=0)

        # transform data
        df = get_lag_change_rates(
            df[value_col], lag_n, remove_extension(f), fill_freq)

        # merge dataframes
        target_df = target_df.join(df, how="inner")

    return target_df


# Merge sets of datas
def merge_datasets(paths, value_columns, lag_configs):
    # param types: list, list, list
    # return pandas.datafraem
    merge_df = pd.DataFrame()
    for i in range(0, len(paths)):
        df = merge_data(
            data_dir=paths[i], value_col=value_columns[i], lag_n=lag_configs[i])

        if(merge_df.empty):
            merge_df = df
        else:
            merge_df = merge_df.merge(df, left_index=True,
                                      right_index=True, how='inner')
    return merge_df
