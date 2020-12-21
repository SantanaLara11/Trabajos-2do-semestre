n=int(input("Cuantas personas hay en total: "))
x=1
suma=0

while x<=n:
    altura=float(input("Ingresa la altura: "))
    suma=suma + altura
    x=x + 1

promedio=suma/n
print(f"La altura promedio es: {promedio}")