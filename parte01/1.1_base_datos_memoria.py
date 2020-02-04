import sqlite3
import pandas as pd

conexion = sqlite3.connect(':memory:')
cursor = conexion.cursor()

sql_tabla_estudiante = "CREATE TABLE estudiante(carnet TEXT, nombre TEXT, apellido TEXT, carrera TEXT, semestre INT, CONSTRAINT carnet_pk PRIMARY KEY (carnet))"

cursor.execute(sql_tabla_estudiante)

sql_consulta_tablas = "SELECT * FROM SQLite_master WHERE type=\"table\""

cursor.execute(sql_consulta_tablas)

print('Tablas disponibles en la base de datos:')

tablas = cursor.fetchall()

for t in tablas:
    print('Nombre tipo objeto en la BD:', t[0])
    print('Nombre objeto BD:', t[1])
    print('Nombre tabla:', t[2])
    print('Sentencia SQL:', t[4])

print()

datos = [('1001', 'Edward', 'Ortiz', 'Informática', 5),
('1002', 'Daniela', 'Ordoñez', 'Arte', 3),
('1003', 'Germán', 'Meneses', 'Programación', 7),
('1004', 'Oliva', 'Urbano', 'Música', 5)]

try:
    sql = '''INSERT INTO estudiante (carnet, nombre, apellido, carrera, semestre) VALUES (?, ?, ?, ?, ?)'''

    cursor.executemany(sql, datos)
except sqlite3.IntegrityError as e:
    print('Error SQLite:', e.args[0])

conexion.commit()

sql = "SELECT * FROM estudiante WHERE carnet='1004'"
cursor.execute(sql)
resultado = cursor.fetchall();
print(resultado)

print()

# Convertir datos de la BD en un archivo CSV:
sql = "SELECT * FROM estudiante"
df = pd.read_sql_query(sql, conexion)
df.to_csv('parte01/estudiantes.csv', index=False)
