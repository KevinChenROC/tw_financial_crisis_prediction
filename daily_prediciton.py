#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
from keras.models import load_model

import config
from models import params
from models.utils.sequence_data import generate_samples_from_data


# In[14]:


# load model and prepare up-to_date data
dataset = pd.read_csv(config.LATEST_DATA_FOR_MODEL_PATH,
                      header=0, parse_dates=[0], index_col=0)

model = load_model("models/"+params.BEST_MODEL_PATH)


# In[15]:


samples = generate_samples_from_data(dataset.to_numpy(),
                                     params.LOOKBACK,
                                     params.STEP,
                                     range(len(dataset)-params.LAST_N_SEQUENCE, len(dataset)))

assert(np.all(dataset[-params.LAST_N_SEQUENCE:].to_numpy()
              == samples[-1][-params.LAST_N_SEQUENCE:]))


# In[41]:


def print_predictions(predictions, time_indexes, last_n_sequence):
    for i in range(len(predictions)):
        print('\n'+'*'*20)
        print("Probability of crisis from {0} is {1}".format(
            time_indexes[i-last_n_sequence], predictions[i]))


# In[42]:


print_predictions(model.predict(samples),
                  dataset.index, params.LAST_N_SEQUENCE)
