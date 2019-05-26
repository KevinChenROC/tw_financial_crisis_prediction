import pandas as pd
import numpy as np

from ..util.lag_value import calc_lag_values
from ..util.calc_rate import calc_simple_rates


def test_calc_lag_values(change_rates):
    lag_n = 2
    lag_values = calc_lag_values(
        change_rates, lag_n, "TGBRATE")
    lag_values = lag_values.dropna()

    for i in range(lag_n, len(lag_values)):
        assert lag_values.iat[i, lag_n-1] == lag_values.iat[i-1, lag_n-2]
        assert lag_values.iat[i, 0] == change_rates[lag_values.index[i-1]]


def run_tests():
    df = pd.read_csv("datasets/raw_data/bond_yield_indexes/TGBRATE.csv",
                     header=0, parse_dates=[0], index_col=0)

    change_rates = calc_simple_rates(df['Value'])
    test_calc_lag_values(change_rates)
