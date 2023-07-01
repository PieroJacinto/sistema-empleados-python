import sqlite3
from flask import Flask,  jsonify, request

# Configurar la conexión a la base de datos SQLite
DATABASE = 'inventario2.db'

def get_db_connection():
    print("Obteniendo conexión...") # Para probar que se ejecuta la función
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Crear la tabla 'productos' si no existe
def create_table():
    print("Creando tabla productos...") # Para probar que se ejecuta la función
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
         CREATE TABLE IF NOT EXISTS empleados (
            id INT NOT NULL ,
            nombre varchar(255),
            correo varchar(255),
            foto varchar(5000)         
        ) ''')
    conn.commit()
    cursor.close()
    conn.close()

# Verificar si la base de datos existe, si no, crearla y crear la tabla
def create_database():
    print("Creando la BD...") # Para probar que se ejecuta la función
    conn = sqlite3.connect(DATABASE)
    conn.close()
    create_table()

# Programa principal
# Crear la base de datos y la tabla Productos si no existen
create_database()


# -------------------------------------------------------------------
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
    def listar_empleados(self):
        print("-"*50)
        print("Empleados - Lista de empleados:")
        print("id\tNombre\tCorreo\tfoto")
        self.cursor.execute("SELECT * FROM empleados")
        rows = self.cursor.fetchall()
        for row in rows:
            id, nombre, correo, foto = row
            print(f'{id}\t{nombre}\t{correo}\t{foto}')
        print("-"*50)
    def consultar_empleado(self, id):
        sql = f'SELECT * FROM empleados WHERE id = {id};'
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        if row:
            id, nombre, correo, foto = row
            return Empleado(id, nombre, correo, foto)
        return False
    def agregar_empleado(self, id, nombre, correo, foto):
        empleado_existente = self.consultar_empleado(id)
        if empleado_existente:
            print("Ya existe un empleado con ese id.")
            return False
        nuevo_empleado = Empleado(id, nombre, correo, foto)
        sql = f'INSERT INTO empleados VALUES ({id},"{nombre}","{correo}", "{foto}");'
        self.cursor.execute(sql)
        self.conexion.commit()
        return True

# Programa principal
# Crear la base de datos y la tabla si no existen
create_database()

# Crear una instancia de la clase Inventario
mis_empleados = Empleados()

mis_empleados.agregar_empleado(1,"piero jacinto", "piero@gmail.com","foto")

mis_empleados.listar_empleados()



