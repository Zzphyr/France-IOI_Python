### 1-3: Calculs et découverte des variables ###

# 1) Réponds !

print(42)

# 2) L'éclipse

print(12581-11937)

# 3) Bonbons pour tout le monde !

print(3*(25+30+27+22-8))

# 4) L'algoréathlon

day=2+34+6
day1=day
day2=day1+day
day3=day2+day
print(day1,day2,day3)

# 5) Cour de récréation

length=5*17+2*7+5+2*2
print(length*length)
print(length*4)

# 6) Une partie de cache-cache

for rob in range(1, 101):
   print (rob)
rob = "J'arrive !"
print(rob)

# 7) Progresser par l'erreur

print("V")
print("V")
print("I")
print("I")
print("V")
print("I")
print("I")

# 8) Décollage de fusée

count=100
for a in range(101):
   print(count)
   count=count-1
print("Décollage !")

# 9) Invasion de batraciens

toad=1337
for a in range(12):
   toad=toad*2
print(toad)

# 10) Kermesse

candy=0
for a in range(1,51):
   candy=candy+a
   print(candy)

# 11) Course avec les enfants

from robot import *
turn=1
for a in range(10):
   for b in range(0,turn):
      droite()
   ramasser()
   for b in range(0,turn):
      gauche()
   deposer()
   turn=turn+1

# 12) Construction d'une pyramide

side=1
total=0
for a in range(9):
    volume=side*side*side
    total=total+volume
    side=side+2
print(total)

# 13) Table de multiplication

numOne=1
numTwo=1
for a in range(20):
    for b in range(20):
        print(numOne*numTwo, end=" ")
        numTwo=numTwo+1
    print()
    numOne=numOne+1
    numTwo=1


## end ##
