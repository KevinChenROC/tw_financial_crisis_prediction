import datetime

# Stock ai config
START_DATE = "1996-01-01"
END_DATE = str(datetime.date.today())
R_KEY = "bN9aBd1PzA"

RETURN_DISTR_WINDOW = 201
MARKET_CRASH_THRESHOLD = 0.03

# paths below are relative to the folder 'tw_crisis_prediction'
DATASETS_PATH = 'datasets/'
RAW_DATA_PATH = "datasets/raw_data/"
SYMBOLS_PATH = "datasets/symbols/"

# paths for raw data folders
STOCK_INDX_PATH = RAW_DATA_PATH + "stock_indexes/"
FOREX_PATH = RAW_DATA_PATH + "forex/"
BOND_INDX_PATH = RAW_DATA_PATH + "bond_yield_indexes/"
MACRO_INDTRS_PATH = RAW_DATA_PATH + "macro_indicators_monthly/"
BISR_PATH = RAW_DATA_PATH + "bisr/"

# path for data to train and predict on
DATA_FOR_MODELS_PATH = DATASETS_PATH + "data_for_models/"
