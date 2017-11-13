import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

df = pd.read_csv('listings.csv', low_memory=False)
df['price'] = df['price'].map(lambda x: x[1:].replace(',', '')).astype(float)
df.plot.scatter(x='accommodates', y='price')
plt.xlabel('Number of People Accommodated')
plt.ylabel('Price ($)')
plt.title('Price vs. Number Accommodated')
plt.savefig('NumAccommodatedVsPrice.png')

plt.figure(1)
df = pd.read_csv('calendar_available_only.csv', low_memory=False)
df['date'] = df['date'].map(lambda x: x[5:7]).astype(float)
df['price'] = df['price'].map(lambda x: x[1:].replace(',', '')).astype(float)
df.plot.scatter(x='date', y='price')
plt.xlabel('Month')
plt.ylabel('Price ($)')
plt.title('Price vs. Month')
plt.savefig('PricevsMonth.png')

plt.figure(2)
df.hist('date', color='lightblue')
plt.xlabel('Month')
plt.ylabel('# of Available Listings')
plt.title('Frequency of Available Listings by Month')
plt.gcf().subplots_adjust(left=0.15)
plt.savefig('Histogram.png')
plt.show()