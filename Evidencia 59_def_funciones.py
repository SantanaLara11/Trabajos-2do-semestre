def presentacion():
    print("Programa que permite cargar dos valores por el usuario.")
    print("Realiza la suma de los valores")
    print("Imprime el resultado de la suma")
    print("---------------------------------")

def carga_suma():
    valor1=int(input("Ingresa el primer valor:"))
    valor2=int(input("Ingresa el segundo valor:"))
    suma=valor1 + valor2
    print("La suma de los dos valores es:",suma)

def finalizar():
    print("--------------------------------------")
    print("Gracias por utilizar el sistema")

#Mandar llamar al programa (Funciones)
presentacion()
carga_suma()
finalizar()

    