import yfinance as yf
import pandas as pd
import numpy as np

nvda = yf.Ticker("NVDA")
nvda_incomestm = nvda.income_stmt
key = "Basic EPS"
# print(type(nvda_incomestm))
print(nvda_incomestm)
print(nvda_incomestm.loc(key))