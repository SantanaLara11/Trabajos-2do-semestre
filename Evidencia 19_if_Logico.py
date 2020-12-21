num1=int(input("Ingresa primer valor: "))
num2=int(input("Ingresa segundo valor: "))
num3=int(input("Ingresa tercer valor: "))

print("El numero mayor es: ")

if num1>num2 and num1>num3:
    print(num1)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)