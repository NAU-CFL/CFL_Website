import datetime as dt
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8

def plot_data(ticker, s_year, e_year):
    start = dt.datetime(int(float(s_year)), 1, 1)
    end = dt.datetime(int(float(e_year)), 1, 1)
    df = web.DataReader(ticker, 'yahoo', start, end)

    p1 = figure(x_axis_type="datetime", title="Stock Closing Prices")
    p1.grid.grid_line_alpha=0.9
    p1.ygrid.band_fill_alpha = 1
    p1.xaxis.axis_label = 'Date'
    p1.yaxis.axis_label = 'Price'
    p1.line(df.index, df['Adj Close'], color='#A6CEE3', legend=ticker)
    p1.legend.location = "top_left"

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(fig)
