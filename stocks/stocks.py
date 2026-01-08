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


# multiple charts

def load_stock(*tickers):
    tickers = [t.strip().upper() for t in tickers]
    data = yf.download(tickers, start = '2010-01-01', end = '2024-12-31')
    data['Open'].plot(figsize= (10,5), title = f'{tickers} Opening prices from 2010 to 2024')
    plt.grid(True)
    plt.ylabel("Price in USD")
    plt.xlabel("Year")
    plt.show()

    
    
    fig, (ax1, ax2,) = plt.subplots(2,1, figsize=(10,6))
    ax1.plot(data["High"])
    ax1.grid(True)
    ax1.set_ylabel('Price in USD')
    # ax1.set_xlabel('Year')
    ax1.set_title(f' Prices at High for {tickers}')

    ax2.plot(data["Volume"])
    ax2.grid(True)
    ax2.set_ylabel('Volume of trade')
    ax2.set_xlabel('Year')
    ax2.set_title(f'Volume of trades for {tickers}')

    fig.tight_layout()
    plt.show()


if __name__ == "__main__" :
    plot_stock('nvda', 'mEta', 'aaPl')
    load_stock('MSFT', 'NDAQ')