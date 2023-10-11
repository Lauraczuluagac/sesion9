import pandas as pd
import streamlit as st

data = pd.read_csv('ventas_vehiculos .csv')

st.header("Tabla antes de la limpieza de datos")
data
#datos vacios
data = data.dropna()

#datos atipicos
#plt.hist(data["Kilometraje"])
#st.pyplot()

#plt.boxplot(data["Kilometraje"])
#st.pyplot()

#data.plot.scatter(x="Estado", y="Kilometraje")
#st.pyplot()

data = data[~((data["Kilometraje"] < 10.000) & (data["Estado"] == "Nuevo"))]
data = data[data["Año"]>2010]

#datos duplicados
duplicates = data[data.duplicated(keep=False)]
#st.write(duplicates)

#formato de datos
#st.write(data.dtypes)
data["Fecha"] = pd.to_datetime(data["Fecha"])
#st.write(data.dtypes)

st.header("Tabla despues de la limpieza de datos")
data