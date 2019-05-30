import pandas as pd

from data_transform.merge_data import merge_datasets
from data_fetching import config
from data_transform.util import crisis_features
from data_transform.util.calc_rate import calc_simple_rates

# TODO Refactor by breaking down this functions


def transform_store_raw_data(dataset_paths, val_columns, lag_configs, raw_data_path):
    # Merge all datasets into one big DF
    target_df = merge_datasets(dataset_paths, val_columns, lag_configs)

    # Get crisis-related features
    tw_stock = pd.read_csv("datasets/raw_data/stock_indexes/^TWII.csv",
                           header=0, parse_dates=[0], index_col=0)
    crisis_df = crisis_features.transform(
        calc_simple_rates(tw_stock['Close']).dropna())

    # Drop Column 'Crisis'
    # merge above dataframes into one DF
    target_df = target_df.join(crisis_df.drop(
        labels='Crisis', axis=1), how='inner')

    # normalize all columns in this DF
    normalized_df = (target_df-target_df.min()) / \
        (target_df.max()-target_df.min())

    # store this DF
    # TODO Make a seperate function for store csv file. store_dataframe(file_ext, df, path)
    train_test_filename = raw_data_path + "train_test_data.csv"
    with open(train_test_filename, 'wb') as file:
        data_to_write = normalized_df.to_csv()
        file.write(data_to_write.encode())

    normalized_df_read = pd.read_csv(train_test_filename,
                                     header=0, parse_dates=[0], index_col=0)

    assert normalized_df_read.size == normalized_df.size
    assert normalized_df_read.columns.size == normalized_df.columns.size


dataset_paths = [config.STOCK_INDX_PATH, config.BOND_INDX_PATH,
                 config.REER_PATH, config.MACRO_INDTRS_PATH]
val_columns = ['Close'] + ['Value'] * 3
lag_configs = [config.DAY_LAG_N] + [config.MONTH_LAG_N]*3

transform_store_raw_data(dataset_paths, val_columns,
                         lag_configs, config.RAW_DATA_PATH)
