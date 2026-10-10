import socket
import ipaddress

pocitac = socket.gethostname()
moje_ip = socket.gethostbyname(pocitac)
print("Tenhle počítač se jmenuje", pocitac, "a má adresu", moje_ip)

adresa = ipaddress.ip_address(moje_ip)
print("Verze protokolu IP:", adresa.version)
print("Je to privátní adresa:", adresa.is_private)
print("Adresa jako jedno číslo:", int(adresa))
print("Adresa binárně:", bin(int(adresa)))