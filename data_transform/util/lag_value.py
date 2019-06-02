import pandas as pd
import numpy as np
from .calc_rate import calc_simple_rates


def calc_lag_values(series, lag_n, symbol):  # return a dataframe with n+1 dimensions
    start_index = 0

    # find the index of first non-NaN
    for i in range(start_index, series.size):
        if(not np.isnan(series[i])):
            start_index = i + lag_n
            break

    # Add (n+1)th date to date index
    date_idx = series.index
    date_idx = date_idx[:-1].append(pd.date_range(
        freq=date_idx.inferred_freq, start=date_idx[-1], periods=2))

    # construct a dataframe for lag values with new date index
    cols = ["lag{0}_{1}".format(i, symbol) for i in range(1, lag_n+1)]
    target_df = pd.DataFrame(index=date_idx, columns=cols)

    # construct lag values
    for i in range(start_index, len(target_df.index)):
        for j in range(0, lag_n):
            target_df.iat[i, j] = series[i-j-1]

    # truncate the rows with NaN in columns
    return target_df.dropna()
