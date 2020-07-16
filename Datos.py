import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash #modulos de Flask
from sqlite3 import Error

app = Flask(__name__)

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

def filter_Medico(Centro = "all",Especialidad = "all"):
    cur = con.cursor()
    cur.execute('''SELECT * FROM Doctores''')
    data = cur.fetchall()
    Datos = []
    if Centro == "all" and Especialidad == "all":
        for i in data:
            Datos.append(i)
    elif Especialidad == "all":
        for i in data:
            if i[4] == Centro:
                Datos.append(i)
    elif Centro == "all":
        for i in data:
            if i[3] == Especialidad:
                Datos.append(i)
    else:
        for i in data:
            if i[3] == Especialidad and i[4] == Centro:
                Datos.append(i)

    print(Datos)

def filter_Centro(Ciudad):
    cur = con.cursor()
    cur.execute('''SELECT * FROM centrosMedicos''')
    data = cur.fetchall()
    Datos = []
    for i in data:
        if i[1] == Ciudad:
            Datos.append(i)
    print(Datos)

@app.route('/')
def Home():
    return render_template('index.html')


@app.route('/Medicos')
def Medicos():
    return render_template('medicos.html')


@app.route('/Centros')
def Centros():
    return render_template('Centros.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Contact')
def Contact():
    return render_template('contact.html')

if __name__ == '__main__':

    app.run(debug = True)
