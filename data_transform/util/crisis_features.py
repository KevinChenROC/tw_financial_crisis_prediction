import pandas as pd
import numpy as np

import config
from .calc_rate import calc_simple_rates
from .stats import ecdf


def get_crisis_label(change_rates):  # return a new df
    change_rates = change_rates.dropna()

    start_idx = config.START_IDX_RETURN_DISTRI
    df = pd.DataFrame(index=change_rates.index, columns=['Crisis'])

    for i in range(start_idx, change_rates.size):
        percentile = ecdf(change_rates[:i].to_numpy(), change_rates[i].item())
        if(percentile < config.MARKET_CRASH_THRESHOLD_PERCENTILE):
            df.at[df.index[i], 'Crisis'] = 1
        else:
            df.at[df.index[i], 'Crisis'] = 0

    return df.dropna()


def crises_in_past_n_days(crisis_labels, past_n_list):  # return a new df
    df = pd.DataFrame(index=crisis_labels.index)
    for past_n in past_n_list:

        col_label = "Past " + str(past_n) + "-day events"
        df[col_label] = np.nan
        start_idx = past_n

        for i in range(start_idx, crisis_labels.size):
            df.at[df.index[i], col_label] = crisis_labels[i -
                                                          past_n:i].where(crisis_labels == 1).dropna().size

    return df.dropna()


def crisis_in_next_n_days(crisis_labels, next_n_list):
    df = pd.DataFrame(index=crisis_labels.index)
    for next_n in next_n_list:

        # construct empty columns
        col_label = "Crisis in next " + str(next_n) + " days"
        df[col_label] = np.nan

        end_idx = crisis_labels.size-next_n-1
        for i in range(0, end_idx):
            next_idx = i+1
            df.at[df.index[i], col_label] = 1 if crisis_labels[next_idx:next_idx +
                                                               next_n].where(crisis_labels == 1).dropna().size > 0 else 0

    return df.dropna()


def transform(change_rates):
    df_list = []

    df_list.append(get_crisis_label(change_rates))  # OK
    df_list.append(crises_in_past_n_days(
        df_list[0], config.PAST_N_DAYS_LIST))
    df_list.append(crisis_in_next_n_days(df_list[0], config.NEXT_N_DAYS_LIST))

    # merge dfs in the list
    merged_df = pd.DataFrame(index=change_rates.index)

    for df in df_list:
        merged_df = merged_df.join(df, how='inner')

    return merged_df
