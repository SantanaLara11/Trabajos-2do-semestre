#62. Desarrollar un programa que solicite la carga de tres valores y
#    muestre el menor.
#    a) Desde el bloque principal del programa llamara 2 veces a dicha
#       función (sin utilizar una estructura repetitiva).
def valor_menor():
    valor1=int(input("Ingresa el primer valor: "))
    valor2=int(input("Ingresa el segundo valor: "))
    valor3=int(input("Ingresa el tercer valor: "))
    
    if valor1<valor2 and valor1<valor3:
        print("El valor menor es: ",valor1)
    
    else:
        if valor2<valor3:
            print("El valor menor es: ",valor2)
        else:
            print("El valor menor es: ",valor3)

valor_menor()
valor_menor()