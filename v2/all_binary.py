from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

dfb = pd.read_csv('dicotomica.csv')
dfb = dfb.sort_values('Num31')
dfb = dfb.groupby('Num31').mean().reset_index()

dfb2 = pd.read_csv('dicotomica2.csv')
dfb2 = dfb2.sort_values('Num32')
dfb2 = dfb2.groupby('Num32').mean().reset_index()

dfb3 = pd.read_csv('dicotomica3.csv')
dfb3 = dfb3.sort_values('Num33')
dfb3 = dfb3.groupby('Num33').mean().reset_index()

s = [.5 for n in range(len(dfb.index))]

ax = dfb.plot.scatter(x='Num31', y='Binary1', s=s, color='blue')
dfb2.plot.scatter(ax=ax, x='Num32', y='Binary2', s=s, color='red')
dfb3.plot.scatter(ax=ax, x='Num33', y='Binary3', s=s, color='green')
ax.ticklabel_format(useOffset=False, style='plain')

# dfb.plot.scatter(x='Num31', y='Binary1', s=s)

plt.xlabel("Mida d'entrada (n)")
plt.ylabel("Temps (s)")

plt.grid('on')

plt.show()
plt.savefig("plot.png")
