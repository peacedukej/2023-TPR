import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from numpy.typing import ArrayLike

import yfinance as yf
tickers = ['RASP.ME', 'GAZP.ME', 'DSKY.ME', 'SBER.ME', 'KMAZ.ME', 'RUAL.ME']
start = '2020-04-01'
end = '2022-04-22'
data = yf.download(tickers, start=start, end=end, interval='1d')
closeprices = data['Close']
closeprices = closeprices.dropna()
print(closeprices)

plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(12, 6))

for ticker in closeprices.columns:
    ax.plot(closeprices.index, closeprices[ticker], label=ticker)

ax.set_title('Котировки акций на протяжении игрового периода')
ax.set_xlabel('Дата')
ax.set_ylabel('Цена закрытия')
ax.legend(loc='upper left')
plt.xticks(rotation=45)

plt.show()

market_returns = closeprices.pct_change().dropna()
print(market_returns)