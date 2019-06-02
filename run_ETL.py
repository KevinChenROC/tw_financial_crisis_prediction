from data_transform.raw_data import transform_raw_data
from data_fetching.data_downloader import download_raw_data
from data_transform.util.store_data import store_dataframe
from data_fetching import config


def start():
    # download raw data
    download_raw_data(config.SYMBOLS_PATH, config.RAW_DATA_PATH)

    # transform
    print("\n Transform and store raw data")
    dataset_paths = [config.STOCK_INDX_PATH, config.BOND_INDX_PATH,
                     config.REER_PATH, config.MACRO_INDTRS_PATH]
    val_columns = ['Close'] + ['Value'] * 3
    lag_configs = [config.DAY_LAG_N] + [config.MONTH_LAG_N]*3

    df_transformed = transform_raw_data(dataset_paths, val_columns,
                                              lag_configs, config.RAW_DATA_PATH)

    # store this DF
    target_file_path = config.DATASETS_PATH + "train_test_data.csv"
    store_dataframe(df_transformed, 'csv', target_file_path)

    print("ETL finished")


start()
