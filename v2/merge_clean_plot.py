import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

dfm = pd.read_csv('merge.csv')
dfm = dfm.sort_values('Num1')
dfm = dfm.groupby('Num1').mean().reset_index()

x = dfm['Num1'].tolist()
y = dfm['Ordenament per barreja'].tolist()

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

s = [1 for n in range(len(x))]

#dfl.plot.scatter(xx, yy)
plt.scatter(x, y, s=s)
#dfm.plot(x='Num1', y='Ordenament per barreja', linewidth=2)
plt.plot(x, mymodel, color='red')

print(r)

plt.title("Complexitat temporal de l'ordenació per barreja")
plt.xlabel("Mida d'entrada (n)")
plt.ylabel("Temps (s)")

plt.grid('on')

plt.show()
plt.savefig("plot.png")
