from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

dfb = pd.read_csv('bubble.csv')
dfb = dfb.sort_values('Num')
dfb = dfb.groupby('Num').mean().reset_index()

dfm = pd.read_csv('merge.csv')
dfm = dfm.sort_values('Num1')
dfm = dfm.groupby('Num1').mean().reset_index()

dfl = pd.read_csv('linear.csv')
dfl = dfl.sort_values('Num2')
dfl = dfl.groupby('Num2').mean().reset_index()

dfy = pd.read_csv('binary.csv')
dfy = dfy.sort_values('Num3')
dfy = dfy.groupby('Num3').mean().reset_index()

s = [1 for n in range(len(dfm.index))]
ss = [1 for n in range(len(dfl.index))]
sss = [1 for n in range(len(dfy.index))]
ssss = [1 for n in range(len(dfb.index))]

ax = dfm.plot.scatter(x='Num1', y='Ordenament per barreja', s=s, color='red')
dfy.plot.scatter(ax=ax, x='Num3', y='Binary', s=sss, color='yellow')
dfl.plot.scatter(ax=ax, x='Num2', y='Linear', s=ss, color='blue')
dfb.plot.scatter(ax=ax, x='Num', y='Ordenament bombolla', s=ssss, color='green')
ax.ticklabel_format(useOffset=False, style='plain')

plt.title("Complexitat temporal dels quatre algoritmes")
plt.xlabel("Mida d'entrada (n)")
plt.ylabel("Temps (s)")

plt.grid('on')

plt.show()
plt.savefig("plot.png")
