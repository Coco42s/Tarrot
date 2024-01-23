import socket
import threading

def gestion_socket(socket_obj):
    while True:
        data = socket_obj.recv(1024)
        if not data:
            break
        print(f"Reçu: {data.decode('utf-8')}")

# Adresse et port du premier serveur
serveur1_addr = ('localhost', 8000)
# Adresse et port du deuxième serveur
serveur2_addr = ('localhost', 9000)

# Création du premier socket
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect(serveur1_addr)

# Création du deuxième socket
socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket2.connect(serveur2_addr)

# Démarrer un thread pour gérer chaque socket
thread_socket1 = threading.Thread(target=gestion_socket, args=(socket1,))
thread_socket2 = threading.Thread(target=gestion_socket, args=(socket2,))

# Démarrer les threads
thread_socket1.start()
thread_socket2.start()

# Attendre que les threads se terminent (ce qui ne se produira jamais dans cet exemple)
thread_socket1.join()
thread_socket2.join()

# Fermer les sockets
socket1.close()
socket2.close()