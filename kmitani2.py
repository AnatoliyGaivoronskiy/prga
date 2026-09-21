import math
import time

znak = "O"
amplituda = 30
rychlost = 0.25
tlumeni = 0.2

for krok in range(200):
    cas = krok * rychlost
    utlum = math.exp(-tlumeni * cas)
    vychylka = math.sin(cas) * utlum
    pozice = int(amplituda + amplituda * vychylka)
    print(" " * pozice + znak + " " * (2 * amplituda - pozice) + "|")
    time.sleep(0.04)
