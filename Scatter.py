import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('data.csv')

x = df['UnitPrice']
y = df['StockCode']

plt.xlabel('UnitPrice ($)', fontsize=18)
plt.ylabel('StockCode', fontsize=16)
plt.scatter(x, y)
plt.plot(x, y)

plt.show()
