import sqlite3

conexion = sqlite3.connect("test1.sqlite3")

consulta = conexion.cursor()
"""
#Extrayendo todas las filas
sql = "SELECT * FROM tabla1"
if (consulta.execute(sql)):
 filas = consulta.fetchall()
 for fila in filas:
  print(fila[0], fila[1], fila[2], fila[3])
"""
codigo=input("Ingrese el código de un artículo:")
cursor=conexion.execute("select NOMBRE,APELLIDO,ESPECIALIDAD,CLINICA_U_HOSPITAL from tabla1 where NOMBRE=?", (codigo, ))
fila=cursor.fetchone()
if fila!=None:
    print(fila)
else:
    print("No existe un artículo con dicho código.")
conexion.close()