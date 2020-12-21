"""Realizar un programa que solicite la carga por teclado de dos numeros,
si el primero es mayor al segundo su suma y diferencia,
en caso contrario informar el multiplicación y la división del primero respecto al segundo."""

num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))

if num1>num2:
    suma=num1+num2
    print(f"La suma de los dos numeros es: {suma}")
    resta=num1-num2
    print(f"La resta de los dos numeros es: {resta}")
    
else:
    multiplicacion=num1*num2
    print(f"La multiplicacion de los dos numeros es: {multiplicacion}")
    division=num1/num2
    print(f"La division de los dos numeros es : {division}")