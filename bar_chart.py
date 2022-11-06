import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('data.csv')

plt.xlabel('UnitPrice ($)', fontsize=18)
plt.ylabel('StockCode', fontsize=16)

#x = df['UnitPrice ($)']
#y = df['StockCode']
#plt.bar(x, y)

plt.show()
