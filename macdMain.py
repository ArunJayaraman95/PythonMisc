import yfinance
import talib
from matplotlib import pyplot as plt

data = yfinance.download('NFLX','2016-1-1','2020-1-1')
data["macd"], data["macd_signal"], data["macd_hist"] = talib.MACD(data['Close'])
fig = plt.figure()
plt.show()