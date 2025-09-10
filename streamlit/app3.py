# Introducción a Pandas
# Es una librería para manipulación de datos
# Permite trabajar con estructuras de datos como DataFrames y Series
import pandas as pd

url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
# Carga de datos
df = pd.read_csv(url)

# Ver las primeras filas del DataFrame
# print(df.head())

# Informacion general
# print(df.info())

# Estadísticas descriptivas
# print(df.describe())

# Visualización con Matplotlib
# Es una librería para crear gráficos y visualizaciones
import matplotlib.pyplot as plt

# Agrupar por día y calcular el promedio de gasto total
# prom_por_dia = df.groupby('day')['total_bill'].mean()
# print(prom_por_dia.head())

# Crear un gráfico de barras
# plt.figure(figsize=(8, 6))
# plt.bar(prom_por_dia.index, prom_por_dia.values, color='skyblue')
# # Titulo
# plt.title('Promedio de Gasto Total por Día')
# # Etiqueta del eje X
# plt.xlabel('Día')
# # Etiqueta del eje Y
# plt.ylabel('Promedio de Gasto Total')
# plt.show()

# Mini dashboard con Streamlit
import streamlit as st

# st.title('Dashboard de Propinas')
# st.write('Dataset de propinas en un restaurante')

# st.dataframe(df)
# st.table(df.describe())

# # Selector interactivo
# dia_seleccionado = st.selectbox('Selecciona un día', df['day'].unique())

# # Filtro dinámico
# df_filtrado = df[df['day'] == dia_seleccionado]

# st.write(f'Datos para el día: {dia_seleccionado}')
# st.dataframe(df_filtrado)

# # Grafico interactivo
# st.bar_chart(df_filtrado.groupby('day')['total_bill'].mean())



# Dashboard final
st.header('Dashboard Final de Propinas')

# KPIs: Metricas clave
kpi1 = df['total_bill'].mean() # Promedio de ganancia total del mes
kpi2 = df['total_bill'].sum() # Suma de la ganancia total del mes
kpi3 = len(df) # df.shape[0]
# kpi4 = df['size'].sum() # Numero de personas atendidas

# Dividir en 3 columnas
col1, col2, col3 = st.columns(3)

with col1:
    st.metric('Ganancia total del mes', round(kpi2, 2))
with col2:
    st.metric('Promedio de ganancia total', round(kpi1, 2))
with col3:
    st.metric('Número de transacciones', kpi3)
# st.metric('Número de personas atendidas', kpi4)


# Filtro por genero
# genero_seleccionado = st.radio('Filtrar por género:', df['sex'].unique())
# df_genero = df[df['sex'] == genero_seleccionado]

# st.write(f'Propinas por género: {genero_seleccionado}')
# st.bar_chart(df_genero.groupby('day')['tip'].mean())

# Filtro combinados
st.sidebar.header('Filtros')
genero_seleccionado = st.sidebar.radio('Filtrar por género:', df['sex'].unique())
dia_seleccionado = st.sidebar.selectbox('Selecciona un día', df['day'].unique())

# Aplicar filtros dinamicos
# Genero: Female, Male
df_filtrado = df[df['sex'] == genero_seleccionado]
# Diay: Thur, Fri, Sat, Sun
df_filtrado = df_filtrado[df_filtrado['day'] == dia_seleccionado]

st.subheader(f'Datos filtrados - Género: {genero_seleccionado}, Día: {dia_seleccionado}')
st.dataframe(df_filtrado)
st.write(f'Total de registros: {df_filtrado.shape[0]}')

# Grafica 1
st.subheader('Promedio de propinas por día')
promedio_propinas = df_filtrado.groupby('day')['tip'].mean()
st.bar_chart(promedio_propinas)

# Grafica 2
st.subheader('Ganancia total por día')
ganancia_total = df.groupby('day')['total_bill'].sum()
st.line_chart(ganancia_total)

# Tabla de resumen
st.subheader('Tabla de Resumen')
resumen = df_filtrado.groupby(['day', 'sex'])[['total_bill', 'tip']].mean().round(2).reset_index()
st.dataframe(resumen)