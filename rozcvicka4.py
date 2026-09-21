import time

sirka = 40

for i in range(sirka):
    print(" " * i + "O")
    time.sleep(0.05)

for i in range(sirka):
    print(" " * (sirka - i) + "O")
    time.sleep(0.05)