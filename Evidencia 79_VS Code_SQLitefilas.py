import sqlite3

conexion=sqlite3.connect("bdpa.db")
precio=float(input("Ingresa un precio: "))
cursor=conexion.execute("select descripcion from articulos where precio>?", (precio,))
filas=cursor.fetchall()
if len(filas)>0:
    for fila in filas:
        print(fila)
else:
    print("No existen articulos con precio mayor al indicado")
conexion.close()