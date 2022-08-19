import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

dfy = pd.read_csv('binary.csv')
dfy = dfy.sort_values('Num3')
dfy = dfy.groupby('Num3').mean().reset_index()

x = dfy['Num3'].tolist()
y = dfy['Binary'].tolist()

s = [1 for n in range(len(x))]

#dfl.plot.scatter(xx, yy)
plt.scatter(x, y, s=s)

plt.title("Complexitat temporal de la cerca dicotòmica")
plt.xlabel("Mida d'entrada (n)")
plt.ylabel("Temps (s)")

plt.grid('on')

plt.show()
plt.savefig("plot.png")
