# Importación de librerías
import streamlit as st # Aplicacion web
import pandas as pd # Manipulación de datos
import matplotlib.pyplot as plt # Visualización de datos
import seaborn as sns # Visualización estadística

# Configuracion principal
st.set_page_config(
    page_title='Dashboard de Sismos'
)

# Titulo
st.title('Dashboard de Sismos en Perú (1960 - 2024)')

st.markdown('Visualización de datos históricos de sismos registrados en Perú entre 1960 y 2024.')

# Cargar datos
df = pd.read_csv('SismosPeru1960_2023.csv')
# Convertir la columna FECHA_HORA a formato datetime
df['FECHA_HORA'] = pd.to_datetime(df['FECHA_HORA'])

# Metricas principales
col1, col2, col3 = st.columns(3)

with col1:
    st.metric('Total de Sismos', df.shape[0])

with col2:
    st.metric('Magnitud Máxima', df['MAGNITUD'].max())

with col3:
    st.metric('Profundidad Promedio(km)', df['PROFUNDIDAD'].mean().round(2))
    

# Graficos principales
col1, col2 = st.columns(2)

with col1:
    st.subheader('Distribución de Magnitudes')
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(df['MAGNITUD'], bins=20, kde=True, color='skyblue', ax=ax)
    # Personalizacion
    ax.set_xlabel('Magnitud')
    ax.set_ylabel('Frecuencia')
    ax.set_title('Histograma de Magnitudes', fontsize=12, fontweight='bold')
    st.pyplot(fig)
    
with col2:
    st.subheader('Clasificacion de Sismos')
    fig, ax = plt.subplots(figsize=(6, 4))
    colores = sns.color_palette('pastel')
    df['CLASIFICACION'].value_counts().plot.pie(
        autopct='%1.1f%%', ax=ax, colors=colores, startangle=90
    )
    ax.set_title('Proporción de Clasificaciones', fontsize=12, fontweight='bold')
    ax.set_ylabel('')
    st.pyplot(fig)


st.subheader('Evolución Temporal de Magnitudes (cantidad)')

df_size = df.groupby(df['FECHA_HORA'].dt.month)['MAGNITUD'].size()

df_size.index = df_size.index.map({
    1:'Ene', 2:'Feb', 3:'Mar', 4:'Abr', 
    5:'May', 6:'Jun', 7:'Jul', 8:'Ago', 
    9:'Set', 10:'Oct', 11:'Nov', 12:'Dic'
})

st.line_chart(df_size)


# Vista de la tabla
st.subheader('Tabla de Datos de Sismos')
st.dataframe(df)