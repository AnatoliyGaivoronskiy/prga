import socket
import time

servery = ["www.seznam.cz", "www.vut.cz", "www.google.com", "www.nic.br", "www.gov.au", "moodle.ssemi.cz", "anatoliygaivoronskiy.github.io"]

for server in servery:
    zacatek = time.perf_counter()
    spojeni = socket.create_connection((server, 443), timeout=5)
    konec = time.perf_counter()
    spojeni.close()
    ms = (konec - zacatek) * 1000
    print(f"{server:<16} {ms:7.1f} ms")