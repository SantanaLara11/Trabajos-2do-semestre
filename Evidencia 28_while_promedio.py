x=1
suma=0

while x<=10:
    valor=int(input("Ingresa el valor: "))
#Acumulador
    suma=suma+valor
#Incrementador 
    x=x+1
#Aqui termina el while
promedio=suma/10
print(f"La suma de los 10 valores es: {suma}")
print(f"El promedio es: {promedio}")