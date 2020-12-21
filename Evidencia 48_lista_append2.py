lista=[]

valor=int(input("Ingresa un valor (Presiona 0 para finalizar): "))

while valor!=0:
    lista.append(valor)
    valor=int(input("Ingresa valor (Presiona 0 para finalizar): "))

print("Tamaño de la lista: ")
print(len(lista))