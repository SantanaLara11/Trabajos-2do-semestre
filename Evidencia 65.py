#65. Desarrollar un programa que permita ingresar el lado de un cuadrado.
#     a) Luego programar si quiere calcular y mostrar su perimetro o su area.
def mostrar_resultado(a,p):
    resultado=input("¿Quieres calcular el area y el perimetro del cuadrado?")
    if resultado=="si":
        print("El area del cuadrado es: ",a)
        print("El perimetro del cuadrado es: ",p)
    else:
        if resultado == "no":
            print("El programa terminó")

def cargar_valor():
    lado=int(input("Ingresa el lado del cuadrado: "))
    area= lado * lado
    perimetro= lado * 4
    mostrar_resultado(area,perimetro)

cargar_valor()
    
    
    
    