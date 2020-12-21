sueldo=int(input("Ingresa el sueldo del empleado: "))
antiguedad=int(input("Ingresa su antiguedad en años: "))

if sueldo<500 and antiguedad>10:
    aumento=sueldo*0.20
    SueldoTotal=sueldo*aumento
    print(f"Tu sueldo total es: {SueldoTotal}")
    
elif sueldo<500:
        aumento=sueldo*0.05
        SueldoTotal=sueldo+aumento
        print(f"Tu sueldo total es: {SueldoTotal}")

elif sueldo>=500:
    print(f"Tu sueldo total es: {sueldo}")