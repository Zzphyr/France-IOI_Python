### 1-4: Lecture de l'entrée ###

# 1) Récoltes

side = int(input())
area=side*side
mass=area*23
print(mass)

# 2) Retraite spirituelle

day=int(input())
second=day*16*60*60
print(second)

# 3) Âge des petits-enfants

âgeCadet = int(input())
âgeAîné = int(input())
différence = âgeAîné - âgeCadet
print(différence)

# 4) Encore des punitions

times=int(input())
for a in range(times):
    print("Je dois suivre en cours")

# 5) Graduation de thermomètres

min=int(input())
max=int(input())
dT=max-min+1
temp=min
for a in range(dT):
    print(temp)
    temp=temp+1

# 6) Jeu de calcul mental

number=66
times=int(input())
multiply=1
for a in range(times):
    number=number*multiply
    print(number)
    multiply=multiply+1

# 7) La Grande Braderie

start=int(input())
wid=int(input())
seller=int(input())
num=start
for a in range(seller+1):
    print(num)
    num=num+wid

# 8) Bétail

num = 0
for a in range(20):
   num=num+int(input())
print(num)

# 9) Socles pour statues

ground=int(input())
top = int(input())
dif = ground-top+1
total=0
side=top
for a in range(dif):
   area=side*side
   total=total+area
   area=0
   side=side+1
print(total)

# 10) Le plus beau Karva

cows=int(input())
for a in range(cows):
    weight=int(input())
    age=int(input())
    horn=int(input())
    height=int(input())
    score=(horn*height)+weight
    print(score)


## end ##
