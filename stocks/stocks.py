import yfinance as yf
from matplotlib import pyplot as plt

# data = yf.download("TSLA", start = '2020-01-01', end = '2024-12-31')

# print(data.head())

# data["High"].plot(figsize = (10,5), title = "Tesla stocks @ high price from 2020 to 2024")
# plt.show()

def plot_stock(*tickers):
    # ticker = ticker.strip().upper()
    tickers = [t.strip().upper() for t in tickers]
    data = yf.download(tickers, start = '2020-01-01', end = '2024-12-31')
    data['Close'].plot(figsize = (10,5), title = f'{tickers}, Closing prices from 2020 to 2024')
    plt.grid(True)
    plt.xlabel("Year")
    plt.ylabel("Price in USD")
    plt.show()

plot_stock('nvda', 'mEta', 'aaPl')

# multiple charts

def load_stock(*tickers):
    tickers = [t.strip().upper() for t in tickers]
    data = yf.download(tickers, start = '2010-01-01', end = '2024-12-31')
    data['Open'].plot(figsize= (10,5), title = f'{tickers} Opening prices from 2010 to 2024')
    plt.grid(True)
    plt.ylabel("Price in USD")
    plt.xlabel("Year")
    plt.show()

    plt.figure(figsize = (10,6))
    
    plt.subplot(2,1,1)
    plt.plot(data["High"])
    plt.grid(True)
    plt.ylabel('Price in USD')
    plt.xlabel('Year')
    plt.title(f' Prices at High for {tickers}')

    plt.subplot(2,1,2)
    plt.plot(data["Volume"])
    plt.grid(True)
    plt.ylabel('Volume of trade')
    plt.xlabel('Year')
    plt.title(f'Volume of trades for {tickers}')

    plt.tight_layout()
    plt.show()

load_stock('MSFT', 'NDAQ')

