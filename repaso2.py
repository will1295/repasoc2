import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('inventario.csv')
serie = df.groupby("Sucursal")["Stock"].sum()

fig,ax = plt.subplots(figsize=(8,5))
ax.bar(serie.index,serie.values,color="blue")
ax.set_title("Stock por sucursal")
ax.set_xlabel("Sucursal")
ax.set_ylabel("Unidades")
plt.show()

