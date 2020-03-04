### 2-2: Découverte des tableaux ###

# 1) Préparation de l'onguent

ingred=[500, 180, 650, 25, 666, 42, 421, 1, 370, 211]
num=int(input())
print(ingred[num])

# 2) Liste de courses

price=[9, 5, 12, 15, 7, 42, 13, 10, 1, 20]
total=0
for a in range(10):
    weight=int(input())
    total=total+weight*price[a]
print(total)

# 3) Grand inventaire

table=[0]*10
transac=int(input())
for a in range(transac):
    item=int(input())
    quant=int(input())
    table[item-1]=table[item-1]+quant
for a in range(10):
    print(table[a])

# 4) Étude de marché

nbProd=int(input())
people=int(input())
array=[0]*nbProd
for a in range(people):
    prefer=int(input())
    array[prefer]=array[prefer]+1
for prod in range(nbProd):
    print(array[prod])

# 5) Répartition du poids

carts=int(input())
caravan=[0]*carts
total=0
for a in range(carts):
    caravan[a]=float(input()) # weight
    total=total+caravan[a]
average=total/carts
for a in range(carts):
    dif=average-caravan[a]
    print(dif)

# 6) Visite de la mine

trips=int(input())
array=[0]*trips
for a in range(trips):
    array[a]=int(input())
for a in range(trips):
    if array[a]==1:
        array[a]=2
    elif array[a]==2:
        array[a]=1
    elif array[a]==4:
        array[a]=5
    elif array[a]==5:
        array[a]=4
inv=[0]*trips
b=trips-1
for a in range(trips):
    inv[a]=array[b]
    b=b-1
    print(inv[a])

# 7) Journée des cadeaux

from math import *
people=int(input())
array=[0]*people
for a in range(people):
    array[a]=int(input())
array.sort()
if (people%2)!=0:
    index=floor(people/2)
    print(array[index])
else:
    index1=int(people/2-1)
    index2=int(people/2)
    print((array[index1]+array[index2])/2)

# 8) Course à trois jambes

people=int(input())
array=[0]*people
for a in range(people):
    array[a]=int(input())
array.sort()
maxind=people-1
arrind=0
paired=[0]*people
for a in range(0,people,2):
    paired[a]=array[arrind]
    paired[a+1]=array[maxind]
    arrind=arrind+1
    maxind=maxind-1
    print("{} {}".format(paired[a],paired[a+1]))

# 9) Banquet municipal

table=int(input())
changes=int(input())
array=[0]*table
for a in range(table):
    array[a]=int(input())
array2=list(array)
for a in range(changes):
    index1=int(input())
    index2=int(input())
    array2[index1]=array[index2]
    array2[index2]=array[index1]
    array=list(array2)
for a in range(table):
    print(array[a])

# 10) Choix des emplacements

location =int(input())
array=[0]*location
for a in range(location):
    array[a]=int(input())
for a in range(location):
    print(array.index(a))


## end ##
