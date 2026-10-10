import time
import urllib.request

adresa = "https://proof.ovh.net/files/10Mb.dat"
print("Stahuji", adresa)

zacatek = time.perf_counter()
data = urllib.request.urlopen(adresa, timeout=60).read()
doba = time.perf_counter() - zacatek

bajtu = len(data)
bitu = bajtu * 8
print(f"Staženo {bajtu / 1_000_000:.1f} MB za {doba:.2f} s")
print(f"Propustnost: {bitu / doba / 1_000_000:.1f} Mbit/s")