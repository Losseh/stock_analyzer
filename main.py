import yfinance as yh

dax = "^GDAXI"
spx = "SPY"
stoxx600 = "XSX6.L"
tickers = dax + " " + spx + " " + stoxx600;

data = yh.download(tickers, start="2020-08-01", end="2020-08-20")
print(data)