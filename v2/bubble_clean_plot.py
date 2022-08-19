import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

dfb = pd.read_csv('bubble.csv')
dfb = dfb.sort_values('Num')
dfb = dfb.groupby('Num').mean().reset_index()

x = dfb['Num'].tolist()
y = dfb['Ordenament bombolla'].tolist()

s = [2 for n in range(len(x))]

#dfl.plot.scatter(xx, yy)
plt.scatter(x, y, s=s)
#dfm.plot(x='Num1', y='Ordenament per barreja', linewidth=2)
# plt.plot(x, mymodel, color='red')

plt.title("Complexitat temporal de l'ordenació bombolla")
plt.xlabel("Mida d'entrada (n)")
plt.ylabel("Temps (s)")

plt.grid('on')

plt.show()
plt.savefig("plot.png")
