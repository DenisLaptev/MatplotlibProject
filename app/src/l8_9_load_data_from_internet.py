import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import urllib
import matplotlib.dates as mdates

# --->required by python
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()


# --->required by python

def bytespdate2num(fmt, encoding='utf-8'):
    # --->required by python
    # strconverter = mdates.strpdate2num(fmt)
    strconverter = mdates.datestr2num
    # --->required by python

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)

    return bytesconverter


def graph_data(stock):
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []

    split_source = source_code.split('\n')

    for line in split_source[1:]:
        stock_data.append(line)

    date, openp, highp, lowp, closep, adjusted_closep, volume = np.loadtxt(stock_data,
                                                                           delimiter=',',
                                                                           unpack=True,
                                                                           # %Y = full year = 2015
                                                                           # %y = partial year = 15
                                                                           # %m = number month
                                                                           # %d = number day
                                                                           # %H = hours
                                                                           # %M = minutes
                                                                           # %S = seconds
                                                                           # 2017-07-25 = %Y-%m-%d
                                                                           converters={0: bytespdate2num('%Y-%m-%d')})

    plt.xlabel('x_Date')
    plt.ylabel('y_ClosePrice')

    plt.title('My title: data from internet')

    plt.plot_date(date, closep, '-', label='ClosePrice')

    plt.legend()
    plt.show()


graph_data('TSLA')
