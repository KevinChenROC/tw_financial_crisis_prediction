from data_transform.transform_raw_data import get_transformed_data
from data_fetching.data_downloader import download_raw_data
from data_transform.util.store_data import store_dataframe
from config import *
from data_transform.util.file_extension import remove_extension

dataset_paths = [STOCK_INDX_PATH, FOREX_PATH] + [BOND_INDX_PATH,
                                                 MACRO_INDTRS_PATH]

# value columns for selecting close prices for each category of data
val_columns = ['Close']*2 + ['Value'] * 2

print("download raw data. Please wait...")
download_raw_data(SYMBOLS_PATH, RAW_DATA_PATH,
                  START_DATE, END_DATE, R_KEY)

print("Transform and store raw data. Please wait...")
df_transformed = get_transformed_data(
    dataset_paths, val_columns, RAW_DATA_PATH, START_DATE, END_DATE, RETURN_DISTR_WINDOW, MARKET_CRASH_THRESHOLD)

assert((len(df_transformed[df_transformed.Crisis == 1]) +
        len(df_transformed[df_transformed.Crisis == 0])) == len(df_transformed))

# store this DF
store_dataframe(df_transformed, 'csv',
                DATASETS_PATH+"train_test_data.csv")

print("ETL finished")
