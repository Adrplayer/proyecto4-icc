#importar modulos

import data # modulos de funciones, SQLite

from flask import Flask, render_template, request, redirect, url_for, flash #modulos de Flask

# inicia la base de datos.
con = data.sql_conection()

# Configuración de pagina (Flask)
app = Flask(__name__)

# ruta / --> inicio de la pagina web
@app.route('/')
def Home():
    return render_template('home.html')


@app.route('/about')
def About():
    return render_template('about.html')
#ordenes
if __name__ == '__main__':

    app.run(debug = True)

    data.extract(con,f='lima')


# ruta /add_contact --> agregar un nuevo objeto a la base de datos.
@app.route('/add_contact', methods = ['POST'] )
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        place = request.form['place']
        city = request.form['city']
        direction = request.form['direction']
        cur = con.cursor()
        cur.execute('INSERT INTO contacto (name , place , city, direction) VALUES (%s, %s, %s, %s)',[name ,place ,city ,direction])
        con.commit()
        return redirect(url_for('Home'))
