import sqlite3
conexion = sqlite3.connect("test1.sqlite3")
consulta = conexion.cursor()
consulta.execute('''CREATE TABLE tabla1
                    (NOMBRE TEXT ,
                    APELLIDO TEXT ,
                    ESPECIALIDAD TEXT ,
                    CLINICA_U_HOSPITAL TEXT)''')
conexion.close()