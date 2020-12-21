cantidad=0
x=1

n=int(input("Numero de piezas analizar: "))

while x<=n:
    largo=float(input("Ingresa la medida de la barra de acero: "))
    if largo>=2.3 and largo<=2.5:
        #acumulador
        cantidad=cantidad+1
        
    #incrementador
    x=x+1

print(f"Cantidad piezas aptas para venta al publico: {cantidad}")