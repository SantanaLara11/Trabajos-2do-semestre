TotalP=int(input("Dime cuantas preguntas te dieron: "))
TotalPC=int(input("Dime cuantas preguntas contestaste correctamente: "))

promedio=(TotalPC/TotalP)*100

if promedio>=90:
    print(f"Tu nivel de porcentaje {promedio} es Máximo")

elif promedio>=75 and promedio<90:
    print(f"Tu nivel de porcentaje {promedio} es Medio")
    
elif promedio>=50 and promedio<75:
    print(f"Tu nivel de porcentaje {promedio} es Regular")
    
elif promedio<50:
    print(f"Tu nivel de porcentaje {promedio} es Fuera de Nivel")

