from lag_values_helper import calc_lag_values
from calc_rate_helper import calc_log_rates, calc_percentage_of
import pandas as pd
import numpy as np


df = pd.read_csv("datasets/raw_data/bond_yield_indexes/TGBRATE.csv",
                 header=0, parse_dates=[0], index_col=0)
df.iloc[:5, 0] = np.nan
df["Growth rate"] = calc_log_rates(df['Value'])
print("#test calc_log_rates")
print(df.head(10))

df = pd.merge(df, calc_lag_values(df['Growth rate'], 2, "TGBRATE"), on='Date')
print("\n#test calc_lag_values")
print(df.head(15))


gdp = pd.read_csv("datasets/raw_data/tw_macro_indicators/TWRGDPNTD.csv",
                  header=0, parse_dates=[0], index_col=0)
extdebt = pd.read_csv("datasets/raw_data/tw_macro_indicators/TWTEXTDEBT.csv",
                      header=0, parse_dates=[0], index_col=0)
print("\n#test calc_ percetage_of")
print(calc_percentage_of(extdebt['Value'], gdp['Value']).head(20))
