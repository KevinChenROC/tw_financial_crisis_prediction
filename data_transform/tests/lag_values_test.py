import pandas as pd
import numpy as np

from ..util.lag_values_helper import calc_lag_values
from ..util.calc_rate_helper import calc_simple_rates, calc_percentage_of

df = pd.read_csv("datasets/raw_data/bond_yield_indexes/TGBRATE.csv",
                 header=0, parse_dates=[0], index_col=0)
df.iloc[:5, 0] = np.nan
df["Growth rate"] = calc_simple_rates(df['Value'])

df = calc_lag_values(df['Growth rate'], 2, "TGBRATE")
print("\n#test calc_lag_values")
print(df.head(15))
