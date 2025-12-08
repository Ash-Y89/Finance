import yfinance as yf
from matplotlib import pyplot as plt
import seaborn as sns

def corr_heatmap(*tickers):
    tickers = [t.strip().upper() for t in tickers]
    data = yf.download(tickers, start = "2020-01-01", end = "2024-12-31")
    returns = data["Close"].pct_change()
    corr = returns.corr()
    sns.heatmap(corr,annot = True, cmap= "coolwarm", linewidths=0.5)
    plt.title(f"Correlation Heatmap: {tickers}")
    plt.show()

corr_heatmap("AAPL", "NDAQ")



    

