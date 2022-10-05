import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

dfb = pd.read_csv('bubble.csv')
dfb = dfb.sort_values('Num')
dfb = dfb.groupby('Num').mean().reset_index()

x = dfb['Num'].tolist()
y = dfb['Ordenament bombolla'].tolist()

s = [3 for n in range(len(x))]

model = np.poly1d(np.polyfit(x,y, 2))
polyline = np.linspace(0, 10000, 10000)

#dfl.plot.scatter(xx, yy)
plt.scatter(x, y, s=s)
#dfm.plot(x='Num1', y='Ordenament per barreja', linewidth=2)
# plt.plot(x, mymodel, color='red')
plt.plot(polyline, model(polyline), color='red')

print(model)

plt.title("Complexitat temporal de l'ordenació bombolla")
plt.xlabel("Mida d'entrada (n)")
plt.ylabel("Temps (s)")

plt.grid('on')

plt.show()
plt.savefig("plot.png")
