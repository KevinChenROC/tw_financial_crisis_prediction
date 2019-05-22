import pandas as pd
import numpy as np

from ..util.calc_rate_helper import calc_simple_rates, calc_percentage_of

df = pd.read_csv("datasets/raw_data/bond_yield_indexes/TGBRATE.csv",
                 header=0, parse_dates=[0], index_col=0)
df.iloc[:5, 0] = np.nan
df["Change rate"] = calc_simple_rates(df['Value'])
print("#test calc_simple_rates")
print(df.head(10))
