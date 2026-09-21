import math
import time

znak = "O"
amplituda = 30
rychlost = 0.05

for krok in range(400):
    cas = krok * rychlost
    vychylka = math.sin(cas)
    pozice = int(amplituda + amplituda * vychylka)
    print(" " * pozice + znak)
    time.sleep(0.04)