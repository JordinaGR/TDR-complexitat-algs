import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

dfl = pd.read_csv('linearlinearmid.csv')
dfl = dfl.sort_values('Num5')
dfl = dfl.groupby('Num5').mean().reset_index()

x = dfl['Num5'].tolist()
y = dfl['LinearLM'].tolist()

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

s = [1 for n in range(len(x))]

#dfl.plot.scatter(xx, yy)
plt.scatter(x, y, s=s)
#dfm.plot(x='Num1', y='Ordenament per barreja', linewidth=2)
plt.plot(x, mymodel, color='red')

print(slope)
print(r)
plt.title("Complexitat temporal de la cerca lineal sent k l'element central")
plt.xlabel("Mida d'entrada (n)")
plt.ylabel("Temps (s)")

plt.grid('on')

plt.show()
plt.savefig("plot.png")
