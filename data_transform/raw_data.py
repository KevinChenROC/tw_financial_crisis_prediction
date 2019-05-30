import pandas as pd

from data_transform.util.merge_data import merge_datasets
from data_fetching import config
from data_transform.util import crisis_features
from data_transform.util.calc_rate import calc_simple_rates


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

    return normalized_df
