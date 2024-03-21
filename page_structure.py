import ticker_data
from datetime import date


def create_page(tickerlist, startdate="2008-01-01", enddate=f"{str(date.today())}"):
    html_content = f"""
    <html>
    <head>
        <title>Historical Prices for Anthony's Assets ({startdate[:4]}-{enddate[:4]})</title>
    </head>
    <body>
    """

    for ticker in tickerlist:
        ticker_data.print_plt(ticker, startdate, enddate)
        information = ticker_data.tracking_data(ticker)
        html_content += f"""
        <section>
        <h1>Ticker data for {ticker} ({startdate[:4]}-{enddate[:4]}):</h1>
        <body>{information[0]}</body>
        <img src = "{ticker}.jpg"><br>
        <small>Previous Close: {information[1]}</small><br>
        <small>Fifty Day Average: {information[2]}</small><br>
        <small>Time Zone: {information[3]}</small>
        </section>
        """
    html_content += """
    </body>
    </html>
    """

    with open(f"assets.html", 'w',errors="ignore") as file:
        file.write(html_content)
