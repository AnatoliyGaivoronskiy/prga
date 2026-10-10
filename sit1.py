import socket

jmeno = input("Jméno serveru (třeba www.seznam.cz): ")
adresa = socket.gethostbyname(jmeno)
print(jmeno, "má IPv4 adresu", adresa)

vsechny = socket.getaddrinfo(jmeno, 443, proto=socket.IPPROTO_TCP)
print("Všechny adresy, které DNS vrátilo:")
for zaznam in vsechny:
    print("  ", zaznam[4][0])