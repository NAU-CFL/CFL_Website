# !/usr/bin/python

import seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data
from argparse import ArgumentParser

def show_stocks(ticker, start, end):
    # Get the data using datareader
    dat = data.DataReader(ticker, 'yahoo', start, end)
    plt.plot(dat['Adj Close'])
    plt.xlabel('Time')
    plt.ylabel('Value of the Company')
    plt.title("Stocks of "+ ticker  )
    plt.grid(True)
    plt.show()




def main():

    # Parse command line options
    parser = ArgumentParser(description="Grabs data from yahoo finance for a company and shows the stock changes")
    parser.add_argument('-t', '--ticker',
			type=str, nargs=1, required=True,
			help='Ticker symbol of the company.')
    parser.add_argument('-s', '--start',
            type=str, nargs=1, required=True,
            help="Start date in this format 1/20/2012")
    parser.add_argument('-e', '--end',
            type=str, nargs=1, required=True,
            help="End date in this format 1/20/2012")

    args = parser.parse_args()

    show_stocks(args.ticker, args.start, args.end)


if __name__ == '__main__':
    main()
