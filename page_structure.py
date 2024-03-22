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
        if startdate[:4] != enddate[:4]:
            range = f"{startdate[:4]}-{enddate[:4]}"
        else:
            range = f"{startdate[:4]}"
        html_content += f"""
        <section>
        <h1>Ticker data for {ticker} ({range}):</h1>
        <body>{information[0]}</body><br>
        <img src = "{ticker}.jpg" width = "1200" height = "800"><br>
        <small>Previous Close: {information[1]}</small><br>
        <small>Fifty Day Average: {information[2]}</small><br>
        <small>Time Zone: {information[3].replace("_", " ")}</small>
        </section>
        """
    html_content += """
    </body>
    </html>
    """

    with open(f"index.html", 'w',errors="ignore") as file:
        file.write(html_content)
