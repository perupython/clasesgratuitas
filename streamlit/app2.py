# BIENVENIDOS A PYTHON PERÚ
# CLASE DE APLICACIONES WEB CON STREAMLIT

# No necesitas HTML, CSS, JS, solo Python
# https://streamlit.io/

# pip install streamlit

import streamlit as st # Framework de aplicaciones web
import pandas as pd # Manipulación de datos
import matplotlib.pyplot as plt # Visualización de datos
import numpy as np # Cálculos numéricos
import seaborn as sns # Visualización estadística

# Título de la aplicación
st.title('Hola Mundo con Streamlit')

# Texto
st.write('Bienvenidos a Python Perú')

# Cómo mostrar un DataFrame
dulces = pd.DataFrame({
    'Producto': ['Galleta', 'Chocolate', 'Caramelo', 'Chicle'],
    'Precio': [1.5, 2.0, 0.5, 0.3],
    'Cantidad': [10, 5, 20, 30],
    'Categoria': ['Dulce', 'Dulce', 'Dulce', 'Dulce']
})

# Mostrar como una tabla estática
st.write('Tabla de Dulces (Estatica)')
st.table(dulces)

frutas = pd.DataFrame({
    'Producto': ['Manzana', 'Banana', 'Naranja', 'Uva', 'Pera', 'Mango', 'Piña', 'Cereza', 'Melón', 'Sandía'],
    'Precio': [0.5, 0.3, 0.7, 1.0, 0.8, 1.5, 2.0, 3.0, 1.2, 1.8],
    'Cantidad': [50, 80, 40, 30, 20, 15, 10, 5, 25, 12],
    'Categoria': ['Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta']
})

# Mostrar como una tabla interactiva
st.write('Tabla de Frutas (Interactiva)')
st.dataframe(frutas.head(4))

# Mostrar Markdown
st.write('## Esto es un subtitulo')
st.write('### Estoy aprendiendo streamlit')
st.write('**Esto es un texto en negrita**')
st.write('Soy un texto normal')

# Mostrar gráfica
st.bar_chart(dulces.set_index('Producto')['Precio'])
# st.line_chart -> lineplot
# st.area_chart -> areaplot

df = pd.concat([dulces, frutas], ignore_index=True)

# Mostrar filtros dinámicos
st.write('### Filtros Dinámicos')
categoria = st.selectbox('Selecciona una categoria', df['Categoria'].unique())
filtro = df[df['Categoria'] == categoria]

st.dataframe(filtro)

# Cargar un archivo CSV

st.write('### Cargar un archivo CSV')

archivo = st.file_uploader('Sube tu archivo', type=['csv'])

if archivo is not None:
    sismos = pd.read_csv(archivo)
    st.write('Datos cargados correctamente')
    st.dataframe(sismos)
    st.dataframe(sismos.describe())
    st.dataframe(sismos.info())

