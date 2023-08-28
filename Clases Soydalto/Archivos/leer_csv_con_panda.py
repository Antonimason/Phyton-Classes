import pandas as pd

#usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("Archivos\\datos.csv")
df2 = pd.read_csv("Archivos\\datos.csv")

#obteniendo los datos de la columna nombre
print(df["nombre"])

#ordenamos el dataframe por la edad
df_orden_ascendete = df.sort_values("edad")

#ordenandolo de forma descendete
df_orden_descendente = df.sort_values("edad", ascending=False)

#concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a las primeras 3 filas con head()
primer_fila = df.head(3)

#accediendo a las ultimas 3 filas con tail()
primer_fila = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del dataframe:
df_info = df.describe()

#accediendoa un elemento especifico del df con loc
elemento_especifico_loc = df.loc[2,"edad"]

#accediendoa un elemento especifico del df con iloc
elemento_especifico_loc = df.iloc[2,2]

#accediendo a todas las filas de una columna
apellidos_loc = df.loc[:,"apellido"]

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]>30,:]

print(mayor_que_30)
