import random

valorC=int(input("Ingrese el valor de su compra: "))
if valorC>=50000:
    print("Puedes participar")
else: 
    print("No puedes participar")

bc = input("Listo para sacar la bolita")
desc=random.randrange(1,4)
total1=valorC*0.10
total2=valorC*0.30
total3=valorC*0.50
if desc==1:
    print("Su descuento es del 10% pues ha sacado la bolita roja" )
    print("El total de su compra es: ", total1)
elif desc==2:
    print("Su descuento es del 30% pues has sacado la bolita azul")
    print("El total de su compra es: ", total2)
elif desc==3:
    print("Su descuento es del 50%")
    print("El total de su compra es: ", total3)
else: 
    print("Su compra es gratis")
