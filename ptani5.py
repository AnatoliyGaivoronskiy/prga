nazev = input("Výrobek: ")
cena = float(input("Cena bez DPH: "))
s_dph = cena * 1.21

print(f"{nazev} stojí {cena:.2f} Kč bez DPH a {s_dph:.2f} Kč s DPH.")

print()
print(f"{'Výrobek':<20}{'bez DPH':>10}{'s DPH':>10}")
print(f"{'Myš Logitech M185':<20}{349:>10.2f}{349 * 1.21:>10.2f}")
print(f"{'Klávesnice Genius':<20}{599:>10.2f}{599 * 1.21:>10.2f}")
print(f"{nazev:<20}{cena:>10.2f}{s_dph:>10.2f}")
print(f"{'Celkem k úhradě':<20}{s_dph:>10.2f} Kč")