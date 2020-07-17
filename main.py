import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash #modulos de Flask
from sqlite3 import Error

app = Flask(__name__)

app.secret_key = 'mysecretkey'

@app.route('/add_Medico',methods = ['POST'])
def add_Medico():
    with sqlite3.connect('Datos-Medicos') as con:
        Nombre = request.form['Nombre']
        Apellido = request.form['Apellido']
        Especialidad = request.form['Especialidad']
        Centro = request.form['Centro']
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
            flash("3")
            return redirect(url_for('Home'))
        else:
            flash("2")
            return redirect(url_for('Home'))

@app.route('/add_Centro',methods = ['POST'])
def add_Centro():
    with sqlite3.connect('Datos-Medicos') as con:
        if request.method == 'POST':
            Nombre = request.form['Nombre']
            Ciudad = request.form['Ciudad']
            Dirección = request.form['Dirección']
            cur = con.cursor()
            Datos = (Nombre, Ciudad, Dirección)
            cur.execute('''INSERT INTO centrosMedicos(Nombre, Ciudad, Dirección) VALUES(?, ?, ?)''', Datos)
            con.commit()
            flash("1")
            return redirect(url_for('Home'))





@app.route('/')
def Home():
    return render_template('index.html')


@app.route('/Medicos/<string:Especialidad>/<string:Centro>')
def show_Medicos(Centro = "all",Especialidad = "all"):
    with sqlite3.connect('Datos-Medicos') as con:
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

        return render_template('medicos.html',Medicos = Datos,Centro = Centro,Especialidad = Especialidad)
@app.route('/Centros/<string:Ciudad>')
def show_Centros(Ciudad = "all"):
    with sqlite3.connect('Datos-Medicos') as con:
        cur = con.cursor()
        cur.execute('''SELECT * FROM centrosMedicos''')
        data = cur.fetchall()
        Datos = []
        if Ciudad == "all":
            for i in data:
                Datos.append(i)
        else:
            for i in data:
                if i[1] == Ciudad:
                    Datos.append(i)
        return render_template('Centros.html',Centros = Datos,Ciudad = Ciudad)

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Contact')
def Contact():
    return render_template('contact.html')

if __name__ == '__main__':

    app.run(debug = True)
