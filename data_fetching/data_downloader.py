from utils.url_maker import make_url_stock_ai
from utils.download_helper import download_file
import os
from os.path import isfile, join
import pandas as pd
import config

# iterate through all symbols csv
symbols_file_paths = [f for f in os.listdir(
    config.SYMBOLS_PATH) if isfile(join(config.SYMBOLS_PATH, f))]

for path in symbols_file_paths:
    print(path[:-4])
    symbols = pd.read_csv(config.SYMBOLS_PATH + path)
    for symbol in symbols.loc[:, 'symbol']:
        download_file(make_url_stock_ai(symbol),
                      config.RAW_DATA_PATH + path[:-4] + "/" + symbol + ".csv")
