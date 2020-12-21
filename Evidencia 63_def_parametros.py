#Funciones con parámetros (variable o asignación de datos)
def mostrar_mensaje(mensaje):
    print("---------------------------")
    print(mensaje)
    print("---------------------------")

def mostrar_suma():
    valor1=int(input("Ingresa el primer valor: "))
    valor2=int(input("Ingresa el segundo valor: "))
    suma= valor1 + valor2
    print("La suma es: ",suma)
    
mostrar_mensaje("El programa muestra la suma de 2 valores")
mostrar_suma()
mostrar_mensaje("Hasta luego")