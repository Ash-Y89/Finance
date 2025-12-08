import yfinance as yf
from matplotlib import pyplot as plt

# data = yf.download("TSLA", start = '2020-01-01', end = '2024-12-31')

# print(data.head())

# data["High"].plot(figsize = (10,5), title = "Tesla stocks @ high price from 2020 to 2024")
# plt.show()

def plot_stock(*tickers):
    # ticker = ticker.strip().upper()
    ticker = [t.strip().upper() for t in tickers]
    data = yf.download(tickers, start = '2020-01-01', end = '2024-12-31')
    data['Close'].plot(figsize = (10,5), title = f'{ticker}, Closing prices from 2020 to 2024')
    plt.grid(True)
    plt.xlabel("Year")
    plt.ylabel("Price in USD")
    plt.show()

plot_stock('nvda', 'meta', 'aaPl')
