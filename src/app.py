from flask import Flask,  jsonify, request
from flask import render_template
from flaskext.mysql import MySQL

import sqlite3

DATABASE = 'inventario2.db'

def get_db_connection():
    print("Obteniendo conexión...") # Para probar que se ejecuta la función
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Crear la tabla 'productos' si no existe
def create_table():
    print("Creando tabla empleados...") # Para probar que se ejecuta la función
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empleados (
            id INT NOT NULL ,
            nombre varchar(255),
            correo varchar(255),
            foto varchar(5000),
            PRIMARY key(id)
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

# Verificar si la base de datos existe, si no, crearla y crear la tabla
def create_database():
    print("Creando la BD...") # Para probar que se ejecuta la función
    conn = sqlite3.connect(DATABASE)
    conn.close()
    create_table()

# Crear la base de datos y la tabla si no existen
create_database()

app = Flask(__name__)


@app.route('/')
def index():   

    return render_template('empleados/index.html')

if __name__ == '__main__':
    app.run( debug = True )