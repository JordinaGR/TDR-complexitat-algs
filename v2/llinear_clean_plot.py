import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

dfl = pd.read_csv('linearlinear.csv')
dfl = dfl.sort_values('Num4')
dfl = dfl.groupby('Num4').mean().reset_index()

x = dfl['Num4'].tolist()
y = dfl['Llinear'].tolist()

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

s = [1 for n in range(len(x))]

#dfl.plot.scatter(xx, yy)
plt.scatter(x, y, s=s)
#dfm.plot(x='Num1', y='Ordenament per barreja', linewidth=2)
# plt.plot(x, mymodel, color='red')

print(slope)

plt.xlabel("Mida d'entrada (n)")
plt.ylabel("Temps (s)")

plt.grid('on')

plt.show()
plt.savefig("plot.png")
