import streamlit as st # Aplicacion web
import pandas as pd # Manipulación de datos
import matplotlib.pyplot as plt # Visualización de datos
import seaborn as sns  # Visualización estadística

# Configuración de la página
st.set_page_config(
    page_title='Dashboard de propinas',
    layout='wide'
)

# Cargar dataset
df = sns.load_dataset('tips')

# Sidebar - Filtros
st.sidebar.header('Filtros')

dias = df['day'].unique() # dias
genero = df['sex'].unique() # genero
propina_min = float(df['tip'].min())
propina_max = float(df['tip'].max())

filtro_dia = st.sidebar.multiselect('Selecciona día de la semana', dias, default=dias)
filtro_genero = st.sidebar.radio('Selecciona género', genero)
rango_propina = st.sidebar.slider('Rango de propina', propina_min, propina_max, (propina_min, propina_max))

df_filtro = df[
    (df['day'].isin(filtro_dia)) &
    (df['sex'].isin([filtro_genero])) &
    (df['tip'].between(rango_propina[0], rango_propina[1]))] # (min, max) -> (2.33, 8.83)

st.title('Dashboard Interactivo de Propinas')

# KPIs
col1, col2, col3, col4 = st.columns(4)

ventas_total = round(df_filtro['total_bill'].sum(), 2)
propinas_total = round(df_filtro['tip'].sum(), 2)
registros = len(df_filtro)
propinas_promedio = round(df_filtro['tip'].mean(), 2) if (registros > 0) else 0

col1.metric('Total de ventas', f'${ventas_total}')
col2.metric('Total de propinas', f'${propinas_total}')
col3.metric('Número de registros', registros)
col4.metric('Propina promedio', f'${propinas_promedio}')

# Visualización de datos
st.subheader('Distribución de Cuentas y Propinas')

col5, col6 = st.columns(2)
with col5:
    fig, ax = plt.subplots()
    sns.histplot(df_filtro['total_bill'], bins=20, kde=True, color='skyblue', ax=ax)
    ax.set_title('Distribución de Total de la Cuenta', fontsize=12, fontweight='bold')
    st.pyplot(fig)

with col6:
    fig, ax = plt.subplots()
    sns.scatterplot(data=df_filtro, x='total_bill', y='tip')
    ax.set_title('Relación entre Total de la Cuenta y Propina', fontsize=12, fontweight='bold')
    st.pyplot(fig)
    

st.subheader('Propinas por Día y Sexo')
col7, col8 = st.columns(2)
with col7:
    fig, ax = plt.subplots()
    sns.boxplot(data=df_filtro, x='day', y='tip', ax=ax)
    ax.set_title('Boxplot de Propinas por Día', fontsize=12, fontweight='bold')
    st.pyplot(fig)

with col8:
    fig, ax = plt.subplots()
    sns.barplot(data=df_filtro, x='day', y='tip', ax=ax)
    ax.set_title('Promedio de Propinas por Día', fontsize=12, fontweight='bold')
    st.pyplot(fig)

st.subheader('Datos filtrados')
st.dataframe(df_filtro )