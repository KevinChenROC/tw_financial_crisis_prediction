# hyperparamters
BATCH_SIZE = 64

# params for generator
DELAY = 10
STEP = 1  # 1 timestep = 1 day
LOOKBACK = 15

# ratio for train/val/test split
TRAIN_RATIO = 0.7
VAL_RATIO = 0.15

# For daily prediction
BEST_MODEL_PATH = './best_model.h5'
LAST_N_SEQUENCE = 3
