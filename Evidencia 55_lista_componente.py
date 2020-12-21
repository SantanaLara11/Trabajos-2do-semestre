lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

#Lista Completa
print(lista)
print("_____________")

#Imprimir el primer componente
print(lista[0])
print("_____________")

#Imprimir el primer valor de la lista
print(lista[0][0])
print("_____________")

#Imprimir la lista de mi primer componente
for x in range (len(lista[0])):
    print(lista[0] [x])
print("_____________")

#Imprimir todos los componentes de la lista
for k in range (len(lista)):
    for x in range (len(lista[k])):
        print(lista[k] [x])
    