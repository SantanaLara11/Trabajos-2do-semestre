import sqlite3

conexion=sqlite3.connect("bdpa.db")
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("refresco", 35.50))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("fritos", 12.50))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("galletas", 8.50))

conexion.commit()
conexion.close()