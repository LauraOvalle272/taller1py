
import random
num1=random.randrange(1,6)
num2=random.randrange(1,6)
print(num1,"y", num2)

if num1==1 and num2==1:
    print("Ganaste pues sacaste un par de uno")
elif num1+num2==3:
    print("Ganaste ya que los dos dados suman 3")
elif num1+num2==11:
    print("Ganaste ya que los dados suman 11")
elif num1==2 or num2==2:
    print("Ganaste ya que sacaste 2")
elif num1==12 or num2==12:
    print("Ganaste ya que sacaste 12")
elif num1+num2==7:
    print("Ganaste pues la suma de los dados es 7")
else: 
    print("llorelo")
