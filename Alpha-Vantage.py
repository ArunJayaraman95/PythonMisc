# Import packages
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

import time

# ticker = input("Input a ticker symbol: ")
ticker = "TSLA"

# api key definitions
api_key = ''
ts = TimeSeries(key=api_key, output_format='pandas')
data_ts, meta_data_ts = ts.get_daily(symbol = ticker, outputsize='full')

# Define and reverse closing list
closingList = list(data_ts['4. close'])
closingList.reverse()

# Shorten closingList to last 400 closes
closingList = closingList[-400:]
# Print reversed closingList
print("CLOSING PRICE LIST", closingList)

# Moving average list
sma50 = []
sma26 = []
sma12= []
macdSma9 = []
ema26 = []
ema12 = []
macdEma9 = []
macd = []

# Simple Moving Average Calculation function
def smaCalc(day, listx):
    for p in range(day - 1, len(closingList) - 1):
        tempS = 0
        for q in range(day):
            tempS += closingList[p - q]
        listx.append(round(tempS / day, 2))

# Calculate SMA for different intervals
smaCalc(26, sma26)
smaCalc(12, sma12)
smaCalc(50, sma50)

# Append sma to ema for corresponding values
ema26.append(sma26[0])
ema12.append(sma12[0])
smaCalc(9, macdSma9)


# Exponential Moving Average Calculation function
def emaCalc(day, listx):
    k = 2/(day + 1)
    for ia in range(1, len(closingList) - 1):
        listx.append(round(((closingList[ia] - listx[ia-1]) * k + listx[ia-1]), 2))

# Calculate ema26 and 12 and print
emaCalc(26, ema26)
emaCalc(12, ema12)
print("EMA26", ema26)
print("EMA12", ema12)

# Calculate the MACD
for i in range(len(ema26) - 1):
    macd.append(round((ema12[i] - ema26[i]), 2))

for p in range(9 - 1, len(macd) - 1):
    tempS = 0
    for q in range(9):
        tempS += closingList[p - q]
    macdSma9.append(round(tempS / 9, 2))

# Shorten ema lists and start macd signal line
ema26 = ema26[-300:]
ema12 = ema12[-300:]
macdEma9.append(macdSma9[0])

km = 2/(9 + 1) # Weight constant

# Calculate macd signal line
for i in range(1, len(macd) - 1):
    macdEma9.append(round(((macd[i] - macd[i-1]) * km + macd[i-1]), 2))
macdEma9 = macdEma9[-300:]
macd = macd[-300:]
macdSignal = macdEma9
print("MACD", macd)
print("MACD Signal", macdSignal)


# Shorten closingList and movingAvg List
closingList = closingList[-300:]
sma50 = sma50[-300:]
print("SMA:", sma50)

print("length is", str(len(closingList)))

# Create the plots
fig, (p2, p1) = plt.subplots(2)
title = "Data for " + ticker
fig.suptitle(title)
p2.plot(closingList, label = "Close")
# p2.plot(sma50, label = "SMA 50")
#
#
p1.plot(macdSignal, label ="Signal")
p1.plot(macd, label = "MACD")
leg1 = plt.legend()

# Intersections
totalTimePeriod = 300

prof = 0

def intersection(x, y):
    intersections = [] # Array of intersections
    insights = [] # Array of decisions (buy/sell)

    for i in range(totalTimePeriod - 1): # Along the array of the first list
        if (x[i+1] <= y[i+1]) != (x[i] <= y[i]): # If there is an intersection
            print(x[i + 1], y[i + 1], x[i + 1] < y[i + 1])
            print(x[i], y[i], x[i] < y[i])
            print("\n")
            if ((x[i+1] > y[i+1]), (x[i] > y[i])) == (True, False): # If 1st goes above 2nd
                print("Sell check")
                print(x[i + 1], y[i + 1], x[i + 1] < y[i + 1])
                print(x[i], y[i], x[i] < y[i])
                print("\n")
                insights.append('sell')  # If 1st goes below 2nd make a sell
                p2.plot(i + 1, closingList[i + 1], 'gx')
                p1.plot(i + 1, macd[i + 1], 'gx')
                global prof
                prof += closingList[i+1]
            else:
                print("Buy check")
                print(x[i + 1], y[i + 1], x[i + 1] < y[i + 1])
                print(x[i], y[i], x[i] < y[i])
                print("\n")
                insights.append('buy')  # Make a buy
                p2.plot(i + 1, closingList[i + 1], 'rx')
                p1.plot(i + 1, macd[i + 1], 'rx')
                prof -= closingList[i + 1]
            intersections.append(i)  # Append the index to intersections
    return intersections, insights # Return the arrays

intersections, insights = intersection(macdSignal, macd)


profit = 0
patience = 2

for i in range(len(intersections) - patience):
    index = intersections[i]
    true_trade = None
    if closingList[index] < closingList[index + patience]: # If the price increase in the interval
        true_trade = 'buy' # TrueTrade is a buy
    elif closingList[index] > closingList[index + patience]: # If the price decreases in the interval
        true_trade = 'sell' # TrueTrade is a sell
    if true_trade is not None: # If there was some trueTrade
        if insights[i] == true_trade: # If the insights equals the true
            profit += abs(closingList[index] - closingList[index + 1]) #Add to the profit
        if insights[i] != true_trade: # Else
            profit += -abs(closingList[index] - closingList[index+1]) # Subtract from the profit

print("Profit:", profit)
print("Profit Update:", prof)
plt.show()
print("Insights:", insights)