import pandas as pd
import numpy as np

from ..util.calc_rate_helper import calc_log_rates, calc_percentage_of

df = pd.read_csv("datasets/raw_data/bond_yield_indexes/TGBRATE.csv",
                 header=0, parse_dates=[0], index_col=0)
df.iloc[:5, 0] = np.nan
df["Growth rate"] = calc_log_rates(df['Value'])
print("#test calc_log_rates")
print(df.head(10))

gdp = pd.read_csv("datasets/raw_data/tw_macro_indicators/TWRGDPNTD.csv",
                  header=0, parse_dates=[0], index_col=0)
reserves = pd.read_csv("datasets/raw_data/tw_macro_indicators/TWFERC.csv",
                       header=0, parse_dates=[0], index_col=0)
print("\n#test calc_ percetage_of")
reserves_gdp = calc_percentage_of(reserves['Value'], gdp['Value'])
print(reserves_gdp.head(20))
