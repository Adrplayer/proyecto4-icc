# Bibliotecas:
import sqlite3
from sqlite3 import Error

#Base de datos a usar:
Base = 'Base.db'

#Conexión sqlite3:
def sql_conection():

    try:
        con = sqlite3.connect(Base)
        print('Conexión establecida con exito:\n \t Base = {}'.format(Base))

        return con

    except Error:

        print(Error)

def sql_table(con):
    cur = con.cursor()
    cur.execute("CREATE TABLE centrosMedicos(id integer PRIMARY KEY, name text, place text, city text, direction text)")
    con.commit()

def add_valors(con):

    cur = con.cursor()
    entities = ('clinica gratuita - san judas iscariote','lima', 'san miguel', 'av los palos 234')
    cur.execute('''INSERT INTO centrosMedicos(name, place, city, direction) VALUES( ?, ?, ?, ?)''', entities)
    con.commit()

def extract(con,f):
    cur = con.cursor()
    cur.execute('SELECT * FROM centrosMedicos')
    x = cur.fetchall()

    for i in x:
        if(i[2] == f):
            print(i)
            print()
