import sqlite3
conexion = sqlite3.connect("test.sqlite3")
consulta = conexion.cursor()
sql = """CREATE TABLE IF NOT EXISTS test( 
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
ciudad VARCHAR(50) NOT NULL,
clinica VARCHAR(50) NOT NULL,
especializacion VARCHAR(50) NOT NULL,
fecha DATE NOT NULL)
"""
if (consulta.execute(sql)):
 print("Tabla creada con éxito")
else: print("Ha ocurrido un error al crear la tabla")
consulta.close()
conexion.commit()
conexion.close()