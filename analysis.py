import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt

START_DATE = '2021/1/1'
END_DATE = '2022/1/1'

meta = data.DataReader('META', 'yahoo', START_DATE, END_DATE)
apple = data.DataReader('AAPL', 'yahoo', START_DATE, END_DATE)
amzn = data.DataReader('AMZN', 'yahoo', START_DATE, END_DATE)
nflx = data.DataReader('NFLX', 'yahoo', START_DATE, END_DATE)
goog = data.DataReader('GOOG', 'yahoo', START_DATE, END_DATE)
