"""Se cargan por teclado tres numeros distintos. Mostrar por pantalla el mayor de ellos."""

num1=int(input("Ingresa el primer valor: "))
num2=int(input("Ingresa el segundo valor: "))
num3=int(input("Ingresa el tercer valor: "))

if num1>num2:
    if num1>num3:
        print(f"El numero mayor es: {num1}")
    else:
        print(f"El numero mayor es: {num3}")
else:
    if num2>num3:
        print(f"El numero mayor es: {num2}")
    else:
        print(f"El numero mayor es: {num3}")