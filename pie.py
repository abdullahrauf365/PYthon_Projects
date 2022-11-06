import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('data.csv')
x = df['Description']
y = df['CustomerID']


plt.pie(y, labels=x, radius=1.2, autopct='%0.01f%%', shadow=True)
plt.show()
