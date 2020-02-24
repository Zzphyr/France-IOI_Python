### 1-8: Répétitions conditionnées ###

# 1) Département de médecine : contrôle d'une épidémie

pop=int(input())
infected=1
day=1
while infected < pop:
    nextDay=infected*2
    infected=infected+nextDay
    day=day+1
print(day))

# 2) Administration : comptes annuels

expense=0
total=0
while expense !=-1:
    expense=int(input())
    if expense!=-1:
        total=total+expense
print(total)

# 3) Département de pédagogie : le « c'est plus, c'est moins »

target=int(input())
tests=1
num=int(input())
while num!=target:
    if num<target:
        print("c'est plus")
    elif num>target:
        print("c'est moins")
    tests=tests+1
    num=int(input())
print("Nombre d'essais nécessaires : ")
print(tests)

# 4) Département d'architecture : construction d'une pyramide

max=int(input())
height=0
total=0
while total <= max:
    height=height+1
    step=height*height
    total=total+step
print(height-1)
print(total-step)

# 5) Département de chimie : mélange explosif

num=int(input())
min=int(input())
max=int(input())
temp=(min+max)/2
count=0
while (temp >= min and temp <= max) and count<num:
    temp=int(input())
    if temp >= min and temp <= max:
        print("Rien à signaler")
    else:
        print("Alerte !!")
    count=count+1


## end ##
