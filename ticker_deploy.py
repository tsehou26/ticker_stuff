from page_structure import create_page
from git_push import acp
from datetime import date


def ticker_deploy(tickerlist, startdate="2008-01-01", enddate=f"{str(date.today())}", index="index.html"):
    create_page(tickerlist, startdate, enddate)
    acp(index)


def main():
    ticker_deploy(["FXAIX", "NVDA", "IBIT"], "2024-01-01")


if __name__ == '__main__':
    main()
