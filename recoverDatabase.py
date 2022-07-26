import sqlite3

def crear_conexion(base_datos):
    try:
        conexion = sqlite3.connect(base_datos)

        return conexion
    except sqlite3.Error as error:
        print('Se ha producido un error al crear la conexión:', error)

def restaurar_copia_seguridad(conexion, archivo):
    with open(archivo, 'r') as f:
        sql = f.read()
    
    try:
        cursor = conexion.cursor()
        cursor.executescript(sql)

        cursor.close()
    except sqlite3.Error as e:
        print('Se ha producido un error al restaurar la base datos:', e)

conexion = crear_conexion('ruta')

nombre_archivo = 'ruta(Copia de seguridad)'
restaurar_copia_seguridad(conexion, nombre_archivo)

if conexion:
    conexion.close()
