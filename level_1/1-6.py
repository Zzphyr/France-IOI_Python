### 1-6: Structures avancées ###

# 1) Villes et villages

num=int(input())
city=0
for a in range(num):
    pop=int(input())
    if pop > 10000:
        city=city+1
print(city)

# 2) Planning de la journée

initial=int(input())
num=int(input())
city=0
for a in range(num):
    village=int(input())
    dist=initial-village
    if dist < 0:
        dist=-dist
    if dist <= 50:
        city=city+1
print(city)

# 3) Étape la plus longue

days=int(input())
max=0
for a in range(days):
    dist=int(input())
    if dist > max:
        max=dist
print(max)

# 4) Calcul des dénivelées

num=int(input())
up=0
down=0
for a in range(num):
    altitude=int(input())
    if altitude > 0:
        up=up+altitude
    else:
        down=down+altitude
print(up)
print(-down)

# 5) Type d'arbres

height=int(input())
leaf=int(input())
if height <= 5 and leaf >=8:
    print("Tinuviel")
elif height >= 10 and leaf >=10:
    print("Calaelen")
elif height <= 8 and leaf <=5:
    print("Falarion")
else:
    print("Dorthonion")

# 6) Tarifs de l'auberge

age=int(input())
weight=int(input())
if age == 60:
    print(0)
elif age < 10:
    print(5)
else:
    if weight < 20:
        print(30)
    else:
        print(40)

# 7) Protection du village

house=int(input())
maxX=int(input())
minX=maxX
maxY=int(input())
minY=maxY
for pos in range(house-1):
    x = int(input())
    y = int(input())
    if x > maxX:
        maxX=x
    elif x < minX:
        minX=x
    if y > maxY:
        maxY=y
    elif y < minY:
        minY=y
horiz=maxX-minX
vert=maxY-minY
perim=2*(horiz+vert)
print(perim)

# 8) Le juste prix

nbMarchands=int(input())
min=1000000
pos=1
for a in range(1,nbMarchands+1):
    prix=int(input())
    if prix < min:
        min=prix
        pos=a
    if prix == min:
        pos=a
print(pos)


## end ##
