import pandas as pd
import numpy as np

from ..util.lag_value import calc_lag_values
from ..util.calc_rate import calc_simple_rates
from data_fetching import config


def test_calc_lag_values(change_rates, symbol, lag_n):
    lag_values = calc_lag_values(
        change_rates, lag_n, symbol)
    lag_values = lag_values.dropna()

    for i in range(lag_n, len(lag_values)):
        assert lag_values.iat[i, lag_n-1] == lag_values.iat[i-1, lag_n-2]
        assert lag_values.iat[i, 0] == change_rates[lag_values.index[i-1]]


def run_tests():
    symbol = "Test"
    df1 = pd.read_csv("datasets/raw_data/bond_yield_indexes/TGBRATE.csv",
                      header=0, parse_dates=[0], index_col=0)

    test_calc_lag_values(calc_simple_rates(df1['Value']), symbol, 3)

    df2 = pd.read_csv(config.STOCK_INDX_PATH + "^N225.csv",
                      header=0, parse_dates=[0], index_col=0)
    test_calc_lag_values(calc_simple_rates(df2['Close']), symbol, 3)

    print("Lag values test finished")
