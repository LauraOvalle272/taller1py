import random 
count=0
total=0
for i in range(1,6,1):
    precio=int(input("ingrese el precio del producto: "))
    cant=int(input("ingrese la cantidad del producto: "))
    count=count+1
    subtotal=precio*cant
    total=total+subtotal 
print("Se registraron", count,"referencias")
print("el total es:",total)

if total>=50000:
    print("Puedes participar")
else: 
    print("No puedes participar")

bc = input("Listo para sacar la bolita")

desc=random.randrange(1,4)

total1=total-(total*0.10)
total2=total-(total*0.30)
total3=total-(total*0.50)

if desc==1:
    print("Su descuento es del 10% pues ha sacado la bolita roja" )
    hs = input("felicidades")
    print("El total de su compra es: ", total1)
    medioP=int(input("Ingrese con que billite paga: "))
    print("su cambio es:", medioP-total1)
elif desc==2:
    print("Su descuento es del 30% pues has sacado la bolita azul")
    hs = input("felicidades")
    print("El total de su compra es: ", total2)
    medioP=int(input("Ingrese con que billite paga: "))
    print("su cambio es:", medioP-total2)
elif desc==3:
    print("Su descuento es del 50% pues has sacado la bolita amarilla")
    hs = input("felicidades")
    print("El total de su compra es: ", total3)
    medioP=int(input("Ingrese con que billite paga: "))
    print("su cambio es:", medioP-total1)
else: 
    print("Su compra es gratis")
    hs = input("felicidades")


