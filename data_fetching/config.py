# Stock ai config
START_DATE = "1996-01-01"
END_DATE = "2019-04-01"
R_KEY = "bN9aBd1PzA"

# Parameters config
DAY_LAG_N = 10
MONTH_LAG_N = 3
QUARTER_N = 2

START_IDX_RETURN_DISTRI = 201
MARKET_CRASH_THRESHOLD_PERCENTILE = 0.03
PAST_N_DAYS_LIST = [5, 20]
NEXT_N_DAYS_LIST = [3, 10]

# paths below are relative to the main folder tw_crisis_prediction
RAW_DATA_PATH = "datasets/raw_data/"
SYMBOLS_PATH = "datasets/symbols/"
STOCK_INDX_PATH = RAW_DATA_PATH + "stock_indexes/"
REER_PATH = RAW_DATA_PATH + "REERs/"
BOND_INDX_PATH = RAW_DATA_PATH + "bond_yield_indexes/"
MACRO_INDTRS_PATH = RAW_DATA_PATH + "macro_indicators_monthly/"
