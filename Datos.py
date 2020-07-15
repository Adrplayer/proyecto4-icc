import sqlite3

from sqlite3 import Error

def sql_connection():

    try:

        con = sqlite3.connect('Datos-Medicos')

        print("Connection is established to Database = 'Datos-Medicos' ")

    except Error:

        print(Error)

    return con
con = sql_connection()

def add_Medico():
    Nombre = input("Nombre del Médico: \n")
    Apellido = input("Apellido del Médico: \n")
    Especialidad = input("Especialidad: \n")
    Centro = input("Centro medico en el cual trabaja: \n")
    cur = con.cursor()
    cur.execute("SELECT Nombre FROM centrosMedicos")
    centros = cur.fetchall()
    Datos = (Nombre,Apellido,Especialidad,Centro)
    cur.execute('''INSERT INTO Doctores(Nombre, Apellido, Especialidad, Centro) VALUES(?,?,?,?)''',Datos)
    Centros = []
    for i in centros:
        Centros.append(i[0])
    print(Centros)
    if Centro in Centros:
        print("centro de atención ya enlistado")
    else:
        print("centro de atención no enlistado")
        add_Centro()
def add_Centro():
    Nombre = input("Nombre del centro Medico: \n")
    Ciudad = input("Ciudad: \n")
    Dirección = input("Dirección: \n")
    cur = con.cursor()
    Datos = (Nombre, Ciudad, Dirección)
    cur.execute('''INSERT INTO centrosMedicos(Nombre, Ciudad, Dirección) VALUES(?, ?, ?)''', Datos)
    con.commit()
    print("Dato agregado")
add_Medico()
