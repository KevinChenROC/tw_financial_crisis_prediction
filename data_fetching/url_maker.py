from config import *
STOCK_AI_URL = "https://stock-ai.com/ddl?s={symbol}&r=" + \
    R_KEY + "&d1=" + START_DATE + "&d2=" + END_DATE


def make_url_stock_ai(symbol):
    # find {sybmol} and replace with the value of symbol variable
    return STOCK_AI_URL.replace("{symbol}", symbol, 1)
