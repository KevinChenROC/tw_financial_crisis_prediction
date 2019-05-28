from ..config import *


def make_url_stock_ai(symbol):
    return "https://stock-ai.com/ddl?s=" + symbol+"&r=" + \
        R_KEY + "&d1=" + START_DATE + "&d2=" + END_DATE
