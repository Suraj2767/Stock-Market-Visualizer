import csv
import numpy as np
import matplotlib.pyplot as plt

dates = []
prices = []

with open("data/stock_data.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        dates.append(row[0])
        prices.append(float(row[1]))

# Statistics
avg_price = np.mean(prices)
max_price = np.max(prices)
min_price = np.min(prices)

print("Average Price =", avg_price)
print("Maximum Price =", max_price)
print("Minimum Price =", min_price)
moving_avg = []

window = 3

for i in range(len(prices)):
    if i < window - 1:
        moving_avg.append(None)
    else:
        avg = np.mean(prices[i-window+1:i+1])
        moving_avg.append(avg)
# Graph
plt.plot(dates, prices, marker='o', label='Price')
plt.plot(dates, moving_avg, marker='s', label='Moving Average')

plt.title("Stock Price Analysis")
plt.xlabel("Date")
plt.ylabel("Price")

plt.xticks(rotation=45)

plt.legend()
plt.grid()

plt.show()