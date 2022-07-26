import sqlite3

try:

    conexion = sqlite3.connect(':memory:')
    print('Se ha establecido una conexión con la base de datos en memoria.')

    sql = 'SELECT sqlite_version();'
    conexion.execute(sql)

    print('Versión de SQLite:', sqlite3.version)

    conexion.close()

except sqlite3.Error as error:
    print('Se ha producido un error:', error)
