import socket

def get_local_ipv4():
    try:
        # Obtient le nom d'hôte de la machine
        host_name = socket.gethostname()

        # Obtient l'adresse IP associée au nom d'hôte
        ip_address = socket.gethostbyname(host_name)

        return ip_address
    except Exception as e:
        print(f"Erreur lors de la récupération de l'adresse IP : {e}")
        return None

# Appel de la fonction pour obtenir l'adresse IP locale
adresse_ip_locale = get_local_ipv4()

if adresse_ip_locale:
    print(f"L'adresse IPv4 de la machine est : {adresse_ip_locale}")
else:
    print("Impossible de récupérer l'adresse IPv4 de la machine.")

