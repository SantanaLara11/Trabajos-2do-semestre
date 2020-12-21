def cargar_suma():
    valor1=int(input("Ingresa el primer valor: "))
    valor2=int(input("Ingresa el segundo valor: "))
    suma=valor1 + valor2
    print("La suma de los valores es: ",suma)

def separacion():
    print("***********************************")
    
#Mandar llamar al programa (funciones)

for x in range(3):
    cargar_suma()
    separacion()
    