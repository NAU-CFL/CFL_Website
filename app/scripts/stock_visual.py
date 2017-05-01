import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data
from bokeh.resources import CDN
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.util.string import encode_utf8

def plot_data(ticker_symbol, start, end):
    dat = data.DataReader(ticker_symbol, 'yahoo',start=start, end=end)
    p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")
    p1.grid.grid_line_alpha=0.9
    p1.ygrid.band_fill_alpha = 1
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'
    p1.line(spaceX.index, dat['Adj Close'], color='#A6CEE3', legend=ticker_symbol)
    p1.legend.location = "top_left"
    # script1, div1 = components(p1)
    return components(p1) 
