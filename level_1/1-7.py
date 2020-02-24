### 1-7: Conditions avancées, opérateurs booléens ###

# 1) Espion étranger

start=int(input())
end=int(input())
people=int(input())
num=0
for a in range(people):
    date=int(input())
    if date >= start and date <= end:
        num=num+1
print(num)

# 2) Maison de l'espion

xmin=int(input())
xmax=int(input())
ymin=int(input())
ymax=int(input())
house=int(input())
num=0
for a in range(house):
    x=int(input())
    y=int(input())
    if x >= xmin and x <= xmax:
        if y >= ymin and y <= ymax:
            num=num+1
print(num)

# 3) Nombre de jours dans le mois

month=int(input())
if month==11:
    print(29)
elif (month<=3) or (month>=7 and month<= 9):
    print(30)
else:
    print(31)

# 4) Amitié entre gardes

start1=int(input())
end1=int(input())
start2=int(input())
end2=int(input())
if end1 < start2 or end2 < start1:
    print("Pas amis")
else:
    print("Amis")

# 5) Nombre de personnes à la fête

total=int(input())
cur=0
max=0
for a in range(total*2):
    movement=int(input())
    if movement > 0:
        cur=cur+1
    else:
        cur=cur-1
    if cur >= max:
        max=cur
print(max)

# 6) Casernes de pompiers

nbpair=int(input())
for a in range(nbpair):
    minx1=int(input())
    maxx1=int(input())
    miny1=int(input())
    maxy1=int(input())
    minx2=int(input())
    maxx2=int(input())
    miny2=int(input())
    maxy2=int(input())
    if maxx1 <= minx2 or maxx2 <= minx1 or maxy1 <= miny2 or maxy2 <= miny1:
        print("NON")
    else:
        print("OUI")

# 7) Personne disparue

nbwanted=int(input())
listSize=int(input())
outside = False
for a in range(listSize):
    num=int(input())
    if num == nbwanted:
        outside=True
if outside:
    print("Sorti de la ville")
else:
    print("Encore dans la ville")

# 8) La grande fête

start=int(input())
end=int(input())
guest=int(input())
spy=0
for a in range(guest):
    arr=int(input())
    dep=int(input())
    susp = (arr>=start and arr<=end) or (dep<=end and dep>=start) or (arr <= start and dep >= end)
    if susp:
        spy=spy+1
print(spy)

# 9) L'espion est démasqué !

people=int(input())
for a in range(people):
    height=int(input())
    age=int(input())
    weight=int(input())
    horse=int(input())
    hair=int(input())
    total=0
    if height>=178 and height <=182:
        total = total+1
    if age >= 34:
        total = total+1
    if weight < 70:
        total = total+1
    if horse==0:
        total = total+1       
    if hair==1:
        total = total+1
    if total==5:
        print("Très probable")
    elif total==3 or total==4:
        print("Probable")
    elif total==0:
        print("Impossible")
    else:
        print("Peu probable")

# 10) Zones de couleurs

allTokens=int(input())
for a in range(allTokens):
    x=int(input())
    y=int(input())
    red1=(x>15 and x<45) and (y>60 and y<70)
    red2=(x>60 and x<85) and (y>60 and y<70)
    smallYellow=(x>25 and x<50) and (y>20 and y<45)
    blue=(x>10 and x<85) and (y>10 and y<55) and not(smallYellow)
    bigYellow=(x>0 and x<90) and (y>0 and y<70) and not(blue) and not(red1) and not(red2)
    if red1 or red2:
        print("Dans une zone rouge")
    elif blue:
        print("Dans une zone bleue")
    elif smallYellow or bigYellow:
        print("Dans une zone jaune")
    else:
        print("En dehors de la feuille")


## end ##
