import pandas as pd

from data_fetching import config
from ..util import crisis_features, calc_rate


def run_crises_in_past_test(crisis_labels):
    past_crises_df = crisis_features.crises_in_past_n_days(
        crisis_labels, config.PAST_N_DAYS_LIST)

    # Match crisis label index with past crises for testing
    crisis_labels = crisis_labels.loc[past_crises_df.index[0]:]

    for i in range(0, len(config.PAST_N_DAYS_LIST)):
        past_crises_sris = past_crises_df.iloc[:, i]
        past_N = config.PAST_N_DAYS_LIST[i]
        for j in range(past_N, len(crisis_labels.index)):
            #     # test if the # of crises in past n days is really true

            assert past_crises_sris[crisis_labels.index[j]] == len(
                crisis_labels[j-past_N:j].where(crisis_labels == 1).dropna())


def run_tests():
    tw_stock = pd.read_csv("datasets/raw_data/stock_indexes/^TWII.csv",
                           header=0, parse_dates=[0], index_col=0)
    crisis_labels = crisis_features.get_crisis_label(
        calc_rate.calc_simple_rates(tw_stock.iloc[0:int(len(tw_stock.index) / 4)]['Close']))

    run_crises_in_past_test(crisis_labels)
    # test crises in past n days & crisis in next n days


run_tests()
