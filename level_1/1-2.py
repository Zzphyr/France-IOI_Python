### 1-2: Répétitions d'instructions ###

# 1) Punition

for loop in range(135):
   print("Je dois respecter le Grand Sorcier.")
   
# 2) Mathématiques de base

for loop in range(13):
   print("9 * 8 = 72")
   
# 3) Transport d'eau

from robot import *
for loop in range(2):
   gauche()
print("Bonjour, laissez-moi vous aider")
ramasser()
for loop in range(32):
   droite()
deposer()

# 4) Le secret du Goma

from robot import *
for loop in range(15):
   droite()
   ramasser()
droite()
deposer()

# 5) Sisyphe

from robot import *
for aaa in range(21):
   haut()
   droite()
for bbb in range(21):
   gauche()
   bas()

# 6) Page d'écriture

for a in range(30):
   print("a_", end="")
print("")
for a in range(30):
   print("b_", end="")
print("")
for a in range(30):
   print("c_", end="")

# 7) Jeu de dames

for a in range(20):
   for a in range(20):
      print("OX", end="")
   print("")
   for a in range(20):
      print("XO", end="")
   print("")

# 8) Mont Kailash

from robot import *
for all in range(108):
   for up in range(13):
      haut()
   for up in range(13):
      droite()
   for up in range(13):
      bas()
   for up in range(13):
      gauche()

# 9) Vendanges

from robot import *
for grapes in range(20):
   ramasser()
   for right in range(15):
      droite()
   deposer()
   for left in range(15):
      gauche()
      
# 10) Le Grand Événement

from robot import *
droite()
for a in range(4):
   for a in range(8):
      droite()
   haut()
   for a in range(8):
      gauche()
   haut()
for a in range(8):
   droite()
haut()
for a in range(9):
   gauche() 
for a in range(9):
   bas()
   

## end ##
