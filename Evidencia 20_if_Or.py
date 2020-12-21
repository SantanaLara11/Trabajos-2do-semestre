dia=int(input("Ingresa el dia: "))
mes=int(input("Ingresa el mes: "))
año=int(input("Ingresa el año: "))

if mes==1 or mes==2 or mes==3:
    print("Corresponde al primer trimestre")
else:
    if mes==4 or mes==5 or mes==6:
        print("Corresponde al segundo trimestre")
    else:
        if mes==7 or mes==8 or mes==9:
            print("Corresponde al tercer trimestre")
        else:
            if mes==10 or mes==11 or mes==12:
                    print("Corresponde al cuarto trimestre")