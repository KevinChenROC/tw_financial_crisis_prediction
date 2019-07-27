import pandas as pd

import config
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


def run_crisis_in_next_test(crisis_labels):
    next_crisis_df = crisis_features.crisis_in_next_n_days(
        crisis_labels, config.NEXT_N_DAYS_LIST)

    for i in range(0, len(config.NEXT_N_DAYS_LIST)):

        # For each column in next_crisis_df
        crisis_in_next_n_day = next_crisis_df.iloc[:, i]
        next_N = config.NEXT_N_DAYS_LIST[i]

        for j in range(0, len(crisis_in_next_n_day.index)-next_N):
            str_idx = crisis_in_next_n_day.index[j+1]
            end_idx = crisis_in_next_n_day.index[j+next_N]
            num_of_next_crises = len(
                crisis_labels.loc[str_idx:end_idx][crisis_labels == 1].dropna())

            if crisis_in_next_n_day.iat[j] >= 1:
                assert num_of_next_crises >= 1
            else:
                assert num_of_next_crises == 0


def run_tests():
    tw_stock = pd.read_csv("datasets/raw_data/stock_indexes/^TWII.csv",
                           header=0, parse_dates=[0], index_col=0)
    crisis_labels = crisis_features.get_crisis_label(
        calc_rate.calc_simple_rates(tw_stock.iloc[0:int(len(tw_stock.index) / 4)]['Close']), config.RETURN_DISTR_WINDOW, config.MARKET_CRASH_THRESHOLD)

    # test crises in past n days & crisis in next n days
    run_crises_in_past_test(crisis_labels)
    run_crisis_in_next_test(crisis_labels)


run_tests()
