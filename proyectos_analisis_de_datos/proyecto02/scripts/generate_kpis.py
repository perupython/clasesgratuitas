# generate_kpis.py

import pandas as pd

df = pd.read_csv('proyectos_analisis_de_datos/proyecto02/data/docentes_clean.csv')


# Calcula métricas base
total_docentes = df['docentes_total'].sum()
total_titulados = df['docentes_con_titulo'].sum()
total_sin_titulo = df['docentes_sin_titulo'].sum()
total_nombrados = df['docentes_nombrados'].sum()
total_contratados = df['docentes_contratados'].sum()

# Calcula porcentajes
pct_titulados = round((total_titulados / total_docentes) * 100, 2)
pct_sin_titulo = round((total_sin_titulo / total_docentes) * 100, 2)
pct_nombrados = round((total_nombrados / total_docentes) * 100, 2)
pct_contratados = round((total_contratados / total_docentes) * 100, 2)

# Estructura en DataFrame
kpi_data = {
    'KPI': [
        'Total docentes',
        '% Docentes titulados',
        '% Docentes sin título',
        '% Docentes nombrados',
        '% Docentes contratados'
    ],
    'Valor': [
        total_docentes,
        pct_titulados,
        pct_sin_titulo,
        pct_nombrados,
        pct_contratados
    ]
}

kpi_df = pd.DataFrame(kpi_data)

print("\nTabla KPI Summary:")
print(kpi_df)

output_path = 'proyectos_analisis_de_datos/proyecto02/data/processed/kpi_summary.csv'
kpi_df.to_csv(output_path, index=False)
