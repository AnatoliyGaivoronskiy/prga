import ipaddress

zapis = input("IP adresa s prefixem (třeba 192.168.1.10/24): ")
rozhrani = ipaddress.ip_interface(zapis)
sit = rozhrani.network

print("Adresa počítače:   ", rozhrani.ip)
print("Adresa sítě:       ", sit.network_address)
print("Maska sítě:        ", sit.netmask)
print("Všesměrová adresa: ", sit.broadcast_address)
print("Adres v síti celkem:", sit.num_addresses, "z toho pro zařízení:", sit.num_addresses - 2)

soused = ipaddress.ip_address(input("Adresa souseda: "))
print("Soused je ve stejné síti:", soused in sit)