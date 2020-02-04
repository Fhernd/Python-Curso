import sqlite3
import pandas as pd

conexion = sqlite3.connect(':memory:')
cursor = conexion.cursor()

sql_tabla_estudiante = "CREATE TABLE estudiante(carnet TEXT, nombre TEXT, apelildo TEXT, carrera TEXT, semestre INT, CONSTRAINT carnet_pk PRIMARY KEY (carnet))"
