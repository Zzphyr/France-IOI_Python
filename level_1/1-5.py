### 1-5: Tests et conditions ###

# 1) Transport des bagages

num=int(input())
weight=int(input())
total = num*weight
if total > 105:
    print("Surcharge !")

# 2) Bornes kilométriques

num1=int(input())
num2=int(input())
if num1 >= num2:
    print(num1-num2)
if num1 < num2:
    print(num2 - num1)

# 3) Tarifs dégressifs

num=int(input())
coin=10
if num > 0:   
    for a in range(num):
        coin=coin+5   
if coin > 53:
    coin = 53
print(coin)

# 4) Bagarre générale

areaArignon=int(input())
areaEvaran=int(input())
dif=areaArignon-areaEvaran
if dif > 10:
    print("La famille Arignon a un champ trop grand")
if dif < -10:
    print("La famille Evaran a un champ trop grand")

# 5) Tarif du bateau

age=int(input())
if age < 21:
    print("Tarif réduit")
else:
    print("Tarif plein")

# 6) Traversée du pont

die1=int(input())
die2=int(input())
total=die1 + die2
if total >= 10:
    print("Taxe spéciale !")
    print(36)
else:
    print("Taxe régulière")
    print(total*2)

# 7) Concours de tir à la corde

num=int(input())
team1=0
team2=0
for a in range(num):
    weight=int(input())
    team1=team1+weight
    weight=int(input())
    team2=team2+weight
if team1 > team2:
    print("L'équipe 1 a un avantage")
else:
    print("L'équipe 2 a un avantage")
print("Poids total pour l'équipe 1 :", team1)
print("Poids total pour l'équipe 2 :", team2)

# 8) Mot de passe du village

num=int(input())
if num == 64741:
    print("Bon festin !")
else:
    print("Allez-vous en !")


## end ##
