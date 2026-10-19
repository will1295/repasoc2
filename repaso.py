import pandas as pd

df = pd.read_csv('inventario.csv')

#Funciones de inspeccion
#head,tail,shape,columns,dtype,info,describe
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())

#Seleccionar y filtrar datos

#print(df[df['Sucursal']=='Sucursal Centro'].head())

print(df[(df['Sucursal']=='Sucursal Centro') & 
         (df['Producto']=='Set de Bolígrafos Gel')].head())


