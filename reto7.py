count=0
import random 
valorG=int(input("Ingrese el valor global: "))
dineroD=int(input("Ingrese la cantidad que desea apostar: "))
if dineroD>valorG:
     print("No puede apostar mas del valor global")
else: 
     print("Bienvenido")
     
contin="s"
while contin=="s" or contin=="S" :

    dineroD=int(input("Ingrese la cantidad que desea apostar: "))
    ele = input("elegir cara o sello \n")
    count=count+1
    if ele == "cara":
        x=0
    else:
        x=1
    resultado = random.randint(0, 1)

    if resultado==0:
         a = "cara"
    else: 
         a = "sello"

    if x==resultado:
         print("ganaste , pues elegiste ", ele, " y salió ", a)
         total=(valorG+dineroD)
         print("Su acumulado es: ",total)
         print("La cantidad de veces que ha jugado son", count)
    else: 
         print("perdiste, pues elegiste ", ele, " y salió ", a)
         total2=(valorG-dineroD)
         print("Su acumulado es: ",total2)
         print("La cantidad de veces que ha jugado son", count)

    contin=input("presione s/S para continuar o n/N para salir: ")



    
         


