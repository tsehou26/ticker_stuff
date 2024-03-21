import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def tracking_data(ticker):
    lst = ['longBusinessSummary', 'previousClose', 'fiftyDayAverage', 'timeZoneFullName']
    stock_info = yf.Ticker(f"{ticker}")
    my_info = [stock_info.info[i] for i in lst]
    return my_info
def print_plt(ticker, startdate, enddate):
    stock_dataframe = pd.DataFrame(yf.Ticker(f"{ticker}").history(start=startdate, end=enddate, interval = "1d"))
    x = stock_dataframe.index
    y = stock_dataframe['Close']
    plt.figure(figsize=(15,10))
    plt.plot(x, y)
    plt.title(f"Price Tracker for {ticker}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.savefig(f"{ticker}.jpg", format="jpg")