import pandas as pd
import numpy as np


def calc_log_rates(series):  # return a series with the same indexes.
    start_index = 0

    # find the index of first non-NaN
    for i in range(start_index, series.size):
        if(not np.isnan(series[i])):
            start_index = i+1
            break

    values = series.tolist()
    rates = []
    for i in range(start_index, len(values)):
        rates.append(np.log(values[i]/values[i-1]))
    return pd.Series(rates, index=series.index[start_index:])


def calc_percentage_of(nomin, denom):  # return a new series
    return nomin/denom
