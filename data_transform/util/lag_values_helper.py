import pandas as pd
import numpy as np
from calc_rate_helper import calc_log_rates


def calc_lag_values(series, lag_n, symbol):  # return a dataframe with n+1 dimensions
    start_index = 0

    # find the index of first non-NaN
    for i in range(start_index, series.size):
        if(not np.isnan(series[i])):
            start_index = i + lag_n
            break

    # construct a new dataframe for lag values, starting from series[start_index]
    cols = ["lag{0}_{1}".format(i, symbol) for i in range(1, lag_n+1)]
    df = pd.DataFrame(index=series.index, columns=cols)

    # construct lag values
    for i in range(start_index, len(series.index)):
        for j in range(0, lag_n):
            df.iat[i, j] = series[i-j-1]

    return df
