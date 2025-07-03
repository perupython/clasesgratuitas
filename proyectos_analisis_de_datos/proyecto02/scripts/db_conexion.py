import psycopg2

dbname = 'analisis_docentes'
user = 'postgres'
password = '6S5uVrKE'
host = 'localhost'
port = '5432'

# Conectarse a la base de datos
try:
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Conexión exitosa a la base de datos")
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM centro_educativo")
    row = cur.fetchall()
    print("Datos de la tabla centro_educativo:")
    for r in row[:10]:
        print(r)
        
    cur.close()
    
    
except psycopg2.Error as e:
    print("Error al conectar a la base de datos:", e)
    
finally:
    if conn:
        conn.close()
        print("Conexión cerrada")