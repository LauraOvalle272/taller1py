
import random 

ele = input("elegir cara o sello \n")

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
else: 
    print("perdiste, pues elegiste ", ele, " y salió ", a)




