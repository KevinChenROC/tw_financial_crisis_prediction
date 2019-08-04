# hyperparamters
BATCH_SIZE = 64

# params for generator
DELAY = 10  # delay is 0 because the target is "crisis in 'next' N days"
STEP = 1  # 1 timestep = 1 day
LOOKBACK = 15

# ratio for train/val/test split
TRAIN_RATIO = 0.7
VAL_RATIO = 0.15
