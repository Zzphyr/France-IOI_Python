### 2-1: Nombres à virgules et autres outils ###

# 1) Origami

paper=0.110
for a in range(15):
    paper=paper*2
print(paper/10)

# 2) Conversions de distances

league=float(input())
km=league/0.707
print(km)

# 3) Comparatif de prix

veggie=int(input())
for a in range(veggie):
    weight=float(input())
    age=float(input())
    price=float(input())
    
    perKg=price/weight
    print(perKg)

# 4) Moyenne des notes

scores=int(input())
total=0
for a in range(scores):
    grade=int(input())
    total=total+grade
average=float(total/scores)
print(average)

# A1)  Augmentation de la population

from math import *
curPop=int(input())
rate=float(input())
futurePop=curPop+curPop*(rate/100)
print(floor(futurePop))

# A2) Construction de maisons

from math import *
need=float(input())
bag=0
kg=60
sum=0
price=45
while sum < need:
    sum=sum+kg
    bag=bag+1
print(price*bag)

# B1) Soirée orageuse

from math import *
time=float(input())
sound=340.29
dist=round((time*sound)/1000)
print(dist)

# B2) Augmentation des taxes

from math import *
tax1=float(input())
tax2=float(input())
price1=float(input())
# I don't understand this formula
noTax= price1 / (1 + tax1/100)
# nor this one, saw them in the net
price2=(1 + tax2/100)*noTax
print(round(price2,2))

# C1) Achat de livres

from math import *
money=float(input())
cost=float(input())
print(floor(money//cost))

# C2) Une belle récolte

person=int(input())
fruit=int(input())
if (fruit%person==0):
    print("oui")
else:
    print("non")

# C3) La roue de la fortune

nbZones=int(input())
print(nbZones % 24)


## end ##
