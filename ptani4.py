minuty = int(input("Kolik minut? "))

hodiny = minuty // 60
zbytek = minuty % 60
print(minuty, "minut je", hodiny, "hodin a", zbytek, "minut.")

vek = int(input("Kolik je ti let? "))
dni = vek * 365
print("Jsi na světě zhruba", dni, "dní, tedy", dni * 24, "hodin.")
print("Za", 18 - vek, "let ti bude 18.")
