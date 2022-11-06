import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
csv_file = 'data.csv'
data = pd.read_csv(csv_file)
CustomerID = data["CustomerID"]
UnitPrice = data["UnitPrice"]

x=[]
y=[]
x=list(CustomerID)
y=list(UnitPrice)

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.hist2d(x, y, bins = (10, 10), cmap = 'cubehelix')

ax2.hist2d(x, y, bins = (200, 200), cmap = 'rainbow')
plt.show()






