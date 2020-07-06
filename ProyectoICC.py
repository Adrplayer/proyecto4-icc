#modulos
import sqlite3

#Conexión
con=sqlite3.connect("mydatabase.db")

# Obtención de datos
n=input("Ingrese la ciudad de la locación del centro médico a agregar:")
m=input("Ingrese el nombre del centro médico:")
o=input("Ingrese la dirección exacta del centro médico:")

print("Gracias por tu colaboración, así ayudarás a más peronas a encontrar un centro médico.")

entities = (n, m , o)
#   Te recomiendo que pongas como nombre en entities (Ciudad, Nombre, Dirección)
#   para que no te estes seguro de datos son, pero no es necesario

#Manejo - Base de datos:
cursorObj=con.cursor()
cursorObj.execute("INSERT INTO centrosmedicos(Ciudad, Nombre, Dirección) VALUES(?, ? ,?)", entities)
con.commit()

#Todo lo demás esta perfecto ;D 
