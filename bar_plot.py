import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')

df = pd.DataFrame(data)

X = list(df.iloc[:, 4])
Y = list(df.iloc[:, 6])

plt.bar(X, Y, color='g')
plt.title("Stock Exchange")
plt.xlabel("Quantity")
plt.ylabel("Unit Price")

plt.show()
