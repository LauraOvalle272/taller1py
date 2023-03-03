import random
piedra=1 
papel=2 
tijera=3
elec1=random.randrange(1,3)
elec2=int(input("Elija 1. para sacar piedra, 2. para sacar papel o 3. para sacar tijera: "))
print("Yo he sacado", elec1, "y tu has sacado" ,elec2)


if elec1==1 and elec2==1 or elec1==2 and elec2==2 or elec1==3 and elec2==3:
    print("Es un empate")
elif elec1==1 and elec2==2:
    print("has ganado pues tu sacaste papel y yo piedra")
elif elec1==3 and elec2==1: 
    print("has ganado pues tu sacaste piedra y yo tijera")
elif elec1==3 and elec2==2:
    print("has ganado pues tu sacaste tijera y yo piedra")
else:
     print("has perdido")