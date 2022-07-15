from this import d
import numpy as np
import pandas as pd
import talib as ta
import pandas_datareader as web
import matplotlib.pyplot as plt
import datetime as dt


START_DATE = '2021/1/1'
END_DATE = '2022/1/1'

data = web.DataReader('AAPL', 'yahoo', START_DATE, END_DATE)

#Simple Moving Average
data['thisIsAColumnName'] = ta.SMA(data['Close'], 100)


