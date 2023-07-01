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

# Definimos la clase empleado
class Empleado:
    def __init__(self, id, nombre, correo, foto):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.foto = foto
        

    def modificar(self, nuevo_id, nuevo_nombre, nuevo_correo, nueva_foto):
        self.id = nuevo_id    
        self.nombre = nuevo_nombre
        self.correo = nuevo_correo
        self.foto = nueva_foto

# definimos la clase empleados

class Empleados:
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()

    def agregar_empleado(self, id, nombre, correo, foto):
        empleado_existente = self.consultar_producto(id)
        if empleado_existente:
            return jsonify({'message': 'Ya existe un empleado con ese id.'}), 400

        #nuevo_producto = Producto(id, correo, foto)
        self.cursor.execute("INSERT INTO empleados VALUES (?, ?, ?, ?, ?)", (id, nombre, correo, foto))
        self.conexion.commit()
        return jsonify({'message': 'Empleado agregado correctamente.'}), 200

    def consultar_producto(self, id):
        self.cursor.execute("SELECT * FROM empleados WHERE id = ?", (id,))
        row = self.cursor.fetchone()
        if row:
            id, nombre, correo, foto = row
            return Empleado(id, nombre, correo, foto)
        return None
    
    def listar_empleados(self):
        self.cursor.execute("SELECT * FROM empleados")
        rows = self.cursor.fetchall()
        empleados = []
        for row in rows:
            id, nombre, correo, foto = row
            empleado = {'id': id, 'nombre': nombre, 'correo': correo, 'foto': foto}
            empleados.append(empleado)
        return jsonify(empleados), 200

app = Flask(__name__)

empleados = Empleados()

@app.route('/')
def index():   
   return empleados.listar_empleados()



if __name__ == '__main__':
    app.run( debug = True )