import sqlite3

nombre=input('Nombre:')
apellido=input('Apellido:')
especialidad=input('Especialidad:')
c1=input('Clinica_U_Hospital:')

conexion = sqlite3.connect("test1.sqlite3")
cursor = conexion.cursor()

cursor.execute('''INSERT INTO tabla1 (NOMBRE, APELLIDO, ESPECIALIDAD, CLINICA_U_HOSPITAL) 
VALUES ('%s','%s','%s','%s')''' %(nombre,apellido,especialidad,c1))
conexion.commit()
conexion.close()