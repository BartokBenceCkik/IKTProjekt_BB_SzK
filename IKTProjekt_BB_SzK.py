# Bartók Bence, Szabó Kornél, 10.b
#Python első beadandó

import math

# Bemenet bekérése
n = int(input("Add meg a mérési pontok számát (n): "))
t = list(map(int, input("Add meg a mért magasságokat (szóközzel elválasztva): ").split()))

# a) Van-e a mért adatok között fennsík?
fennsík = False
for i in range(n):
    if t[i] >= 500:
        print(f"a) Az {i + 1}. mérési pontnál már fennsíkon vagyunk.")
        fennsík = True
        break
    if not fennsík:
        print("a) Nincs fennsík az adatok között.")