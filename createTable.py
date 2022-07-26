import sqlite3

def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)

        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)
    
def crear_tabla(conexion, definicion):
    cursor = conexion.cursor()
    cursor.execute(definicion)
    conexion.commit()


conexion = crear_conexion('ruta a la base de datos')

sql = """
CREATE TABLE usuario(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL
);
"""

crear_tabla(conexion, sql)

if conexion:
    conexion.close()
