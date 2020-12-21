#61. Desarrollar un programa con dos funciones. La primera solicite
 #   el ingreso de un entero y muestre el cuadrado de dicho valor.
 #   a) La segunda que solicite la carga de un valor y muestre el cubo del mismo.
 #   b)Llamar desde el bloque del programa principal a ambas funciones.
def calcular_cuadrado():
    valor=int(input("Ingresa un entero: "))
    cuadrado=valor * valor
    print("El cuadrado del entero es: ",cuadrado)

def calcular_cubo():
    valor=int(input("Ingresa un valor: "))
    cubo= valor * valor * valor
    print("El cubo del valor es: ",cubo)

calcular_cuadrado()
calcular_cubo()
              