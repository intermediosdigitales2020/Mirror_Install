import sqlite3
from sqlite3 import Error
import json
import sys, getopt

''' CONEXION A BASE DE DATOS '''
con = sqlite3.connect('/home/pi/Documents/DigitalSignage/wmm.sqlite')

''' METODO PARA INICIAR CONEXIONES CON LA BASE DE DATOS '''
def sql_connection():
    try:
        con = sqlite3.connect('db.sqlite')
        print("Connection is established!")
    except Error:
        print(Error)
    finally:
        con.close()

''' METODO PARA CREAR LA TABLA IMPACTOS Y SUS RESPECTIVOS INDICES '''
def crear_tabla():
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS impactos(id integer PRIMARY KEY, cliente integer, contador integer)")
    cursorObj.execute("CREATE UNIQUE INDEX IF NOT EXISTS 'impactos_cliente' ON 'impactos' ('cliente')")
    con.commit()

''' METODO QUE CUENTA CUANTOS REGISTROS EXISTEN EN LA TABLA IMPACTOS '''
def contar_registros():
    cursorObj = con.cursor()
    cursorObj.execute("SELECT COUNT(*) FROM impactos")
    result = cursorObj.fetchone()
    number_of_rows = result[0]
    return number_of_rows

''' METODO QUE INICIA LA TABLA IMPACTOS '''
def iniciar_tabla():
    if(contar_registros() != 10):
        cursorObj = con.cursor()
        clientes = [(1,1,0), (2,2,0), (3,3,0), (4,4,0), (5,5,0), (6,6,0), (7,7,0), (8,8,0), (9,9,0), (10,10,0), ]
        cursorObj.executemany("INSERT INTO impactos VALUES (?, ?, ?)", clientes)
        con.commit()

''' METODO QUE RETORNA EL CONTADOR DE IMPACTOS DE UN CLIENTE ESPECIFICO '''
def leer(cliente):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT contador FROM impactos WHERE cliente = ?", (cliente,))
    result = cursorObj.fetchone()
    return result[0]

''' METODO QUE RETORNA UN OBJETO JSON CON LOS CONTADORES DE TODOS LOS CLIENTES '''
def leer_todos():
    cursorObj = con.cursor()
    cursorObj.execute("SELECT cliente, contador FROM impactos")
    result = cursorObj.fetchall()
    return json.dumps(result)

''' METODO QUE INCREMENTA EL CONTADOR DE UN CLIENTE ESPECIFICO '''
def incrementar(cliente):
    count = leer(cliente)
    newCount = count + 1
    cursorObj = con.cursor()
    data = (newCount, cliente)
    cursorObj.execute("UPDATE impactos SET contador = ? WHERE cliente = ?", data)
    con.commit()

''' METODO QUE ACTUALIZA MANUALMENTE EL CONTADOR DE UN CLIENTE ESPECIFICO '''
def actualizar(cliente, contador):
    cursorObj = con.cursor()
    data = (contador, cliente)
    cursorObj.execute("UPDATE impactos SET contador = ? WHERE cliente = ?", data)
    con.commit()

''' METODO POR DEFECTO  QUE INICIA EL PROGRAMA Y MONITOREA LA CONSOLA '''
def main(argv):
    try:
        opts, args = getopt.getopt(argv,"ho:as:u:ti",["help","one=","all","sum=","update=","table","init"])
    except getopt.GetoptError:
        print ('db.py -o :id <one>, -a <all>, -u :id :count <update>')
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help = """
            Uso: db.py [-o, --one] [-a, --all] [-s, --sum] [-u, --update] [-t, --table] [-i, --init]
             
            -o      UNO             Ver contador de un cliente, requiere: ID.
            -a      TODOS           Ver contador de todos los clientes.
            -s      INCREMENTAR     Incrementa en uno (1) el contador de un cliente, requiere: ID.
            -u      ACTUALIZAR      Actualiza el contador de un cliente, requiere: ID,VALOR.
            -t      TABLA           Crea la tabla en la base de datos.
            -i      INICIALIZA      Inicializa la tabla y crea los 15 clientes por defecto.

            Ejemplos:
            >> db.py -o 8
            >> db.py -a
            >> db.py -s 1
            >> db.py -u 2,13
            >> db.py -t
            >> db.py -i
            """
            print (help)
            sys.exit()
        elif opt in ("-o", "--one"):
            print(leer(arg[0]))
        elif opt in ("-a", "--all"):
            print(leer_todos())
        elif opt in ("-u", "--update"):
            values = arg.split(',')
            actualizar(values[0],values[1])
            print('Cliente #'+values[0]+' actualizado a: '+values[1])
        elif opt in ("-s", "--increment"):
            incrementar(arg[0])
            print('Cliente #'+arg[0]+' actualizado')
        elif opt in ("-t", "--table"):
            crear_tabla()
            print('Tabla creada exitosamente.')
        elif opt in ("-i", "--init"):
            iniciar_tabla()
            print('Tabla iniciada exitosamente.')

if __name__ == '__main__':
    main(sys.argv[1:])