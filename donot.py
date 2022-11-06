import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")
print(df.head())
group_size = [sum(df.InvoiceNo), sum(df.Quantity), sum(df.UnitPrice)]

group_labels = ["InvoiceNo\n"+str(sum(df.InvoiceNo)),
                "Quantity\n"+str(sum(df.Quantity)),
                "UnitPrice\n"+str(sum(df.UnitPrice))]
custom_colors = ["skyblue", "yellowgreen", 'tomato']
plt.figure(figsize=(5, 5))
plt.pie(group_size, labels=group_labels, colors=custom_colors)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Assignment 01", fontsize=20)
plt.show()
