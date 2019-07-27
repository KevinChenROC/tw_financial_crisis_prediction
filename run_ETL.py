from data_transform.raw_data import get_train_data
from data_fetching.data_downloader import download_raw_data
from data_transform.util.store_data import store_dataframe
import config
from data_transform.util.file_extension import remove_extension


def start(symbols_path, raw_data_path, dataset_paths, val_columns, target_file_path, data_start_date, data_end_date, r_key):
    # download raw data
    download_raw_data(symbols_path, raw_data_path,
                      data_start_date, data_end_date, r_key)

    # transform raw data into a train test dataset
    print("\n Transform and store raw data")
    df_transformed = get_train_data(
        dataset_paths, val_columns, raw_data_path)

    # store this DF
    store_dataframe(df_transformed, 'csv', target_file_path)

    print("ETL finished")


dataset_paths = [config.STOCK_INDX_PATH, config.FOREX_PATH] + [config.BOND_INDX_PATH,
                                                               config.MACRO_INDTRS_PATH]
val_columns = ['Close']*2 + ['Value'] * 2

start(config.SYMBOLS_PATH, config.RAW_DATA_PATH, dataset_paths,
      val_columns, config.DATASETS_PATH+"train_test_data.csv", config.START_DATE, config.END_DATE, config.R_KEY)
