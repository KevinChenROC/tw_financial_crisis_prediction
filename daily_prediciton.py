#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
from keras.models import load_model

import config
from models import params
from models.utils.sequence_data import data_to_sequences
from models.utils.metrics import print_predictions

# models for prediction
model_paths = [
    "models/" + params.BEST_FC_MODEL_PATH,
    "models/" + params.BEST_LSTM_MODEL_PATH,
]

# read the dataset of economic indicators.
dataset = pd.read_csv(
    config.LATEST_DATA_FOR_MODEL_PATH, header=0, parse_dates=[0], index_col=0
)

# # Collect a list of models
models = []
for model_path in model_paths:
    models.append(load_model(model_path))

## Generate 3 sets of input for the model to produce 3 predictions
sequences = data_to_sequences(
    dataset.to_numpy(),
    params.LOOKBACK,
    params.STEP,
    range(len(dataset) - params.LAST_N_SEQUENCE, len(dataset)),
)

# Test the correction of data_to_sequences function
assert np.all(
    dataset[-params.LAST_N_SEQUENCE :].to_numpy()
    == sequences[-1][-params.LAST_N_SEQUENCE :]
)


# Avg the results of models
for model in models:
    predictions = predictions + (model.predict(sequences) / len(models))

print_predictions(predictions, dataset.index, params.LAST_N_SEQUENCE)
