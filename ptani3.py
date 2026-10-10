nazev = input("Co kupuješ? ")
cena = float(input("Cena za kus (Kč): "))
pocet = int(input("Kolik kusů? "))

bez_dph = cena * pocet
sleva = bez_dph * 0.10
zaklad_dane = bez_dph - sleva
dph = zaklad_dane * 0.12
s_dph = zaklad_dane + dph

print()
print("Položka:", nazev, "×", pocet)
print("Cena bez DPH:", bez_dph, "Kč")
print("Sleva 10 %:", sleva, "Kč")        # <-- Tady jsme přidali výpis slevy
print("Základ po slevě:", zaklad_dane, "Kč") # <-- I mezisoučet
print("DPH 12 %:", dph, "Kč")
print("Celkem k úhradě:", s_dph, "Kč")
