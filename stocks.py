import yfinance as yf

data = yf.download("TSLA", start = '2020-01-01', end = '2020-12-31')

print(data.head())

from matplotlib import pyplot as plt

data["High"].plot(figsize = (10,5), title = "Tesla stocks @ high price from 2020 to 2024")
plt.show()