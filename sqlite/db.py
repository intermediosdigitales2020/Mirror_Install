import sqlite3
from sqlite3 import Error

#con = sqlite3.connect('wmm.db')
#cursorObj = con.cursor()

def sql_connection():
	try:
		con = sqlite3.connect('wmm.db')
		return con
	except Error:
		print(Error)

def crear_tabla():
	con = sql_connection()
	cursorObj = con.cursor()
	cursorObj.execute("CREATE TABLE IF NOT EXISTS impactos(id integer PRIMARY KEY, cliente integer, contador integer)")
	con.commit()
	cursorObj.execute('CREATE UNIQUE INDEX IF NOT EXISTS "impactos_cliente" ON "impactos" ("cliente")')
	con.commit()

def leer(clienteid):
	con = sql_connection()
	cursorObj = con.cursor()
	cursorObj.execute("""SELECT contador FROM impactos WHERE cliente = ?;""", (clienteid,))
	rows = cursorObj.fetchone()[0]
	return rows

def leer_todos():
	con = sql_connection()
	cursorObj = con.cursor()
        cursorObj.execute("""SELECT cliente, contador FROM impactos""")
	rows = cursorObj.fetchall()
        print rows

def actualizar(clienteid):
	con = sql_connection()
	actual = leer(clienteid)
	nuevo = actual + 1
	cursorObj = con.cursor()
	data = (nuevo, clienteid)
	cursorObj.execute("""UPDATE impactos SET contador = ? where cliente = ?;""", data)
	con.commit()
	con.close()

crear_tabla()

