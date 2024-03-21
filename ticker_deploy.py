from page_structure import create_page
from git_push import acp
from datetime import date


def ticker_deploy(tickerlist, startdate="2008-01-01", enddate=f"{str(date.today())}"):
    create_page(tickerlist, startdate, enddate)
    acp("assets.html")


def main():
    ticker_deploy(["FXAIX", "NVDA", "IBIT"])


if __name__ == '__main__':
    main()
