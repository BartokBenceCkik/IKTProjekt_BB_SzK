# Bartók Bence 10.b
#Python első beadandó

import math

# Bemenet bekérése
n = int(input("Add meg a mérési pontok számát (n): "))
t = [int(x) for x in input("Add meg a mért magasságokat (szóközzel elválasztva): ").split()]

# a) Van-e a mért adatok között fennsík?
fennsík = False
for i in range(n):
    if t[i] >= 500:
        print("a) Az {}. mérési pontnál már fennsíkon vagyunk.".format(i + 1))
        fennsík = True
        break
    if not fennsík:
        print("a) Nincs fennsík az adatok között.")

# b) Melyik két pont között volt a legkisebb emelkedési szög?
min_difference = float('inf') # Nagyon nagy szám a kezdéshez
min_index = -1
for i in range(n - 1):
    difference = t[i + 1] - t[i]
    if difference > 0 and difference < min_difference: # Csak emelkedést nézünk
        min_difference = difference
        min_index = i
    if min_index != -1:
        print(f"b) Az {min_index + 1}. mérési pont volt a legkisebb emelkedési szögű.")
    else:
        print("b) Nem volt emelkedés a pontok között.")

# c) Érintett-e a túra során nyerget?
nyereg_van = False

for i in range(1, n):
    if t[i] == t[i - 1]:
        nyereg_van = True
        break

if nyereg_van:
    print("c) Igen, érintett nyerget.")
else:
    print("c) Nem érintett nyerget.")
