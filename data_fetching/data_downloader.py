from .utils.url_maker import make_url_stock_ai
from .utils.download_helper import download_file
import os
from os.path import isfile, join
import pandas as pd
from . import config

# iterate through all symbols csv
symbols_file_paths = [f for f in os.listdir(
    config.SYMBOLS_PATH) if isfile(join(config.SYMBOLS_PATH, f))]

for path in symbols_file_paths:
    target_folder = config.RAW_DATA_PATH + path[:-4] + '/'
    symbols = pd.read_csv(config.SYMBOLS_PATH + path)

    # Make a folder
    try:
        os.mkdir(target_folder)
        print("Create a folder: " + target_folder)
    except FileExistsError:
        print("Donwload data's to " + target_folder)
    except OSError:
        print(OSError)

    for symbol in symbols.loc[:, 'symbol']:

        # Download file to that folder
        download_file(make_url_stock_ai(symbol),
                      target_folder + symbol + ".csv")
