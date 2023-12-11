import socket

host, port = ('127.0.0.1',5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((host, port))
    print("Connect")

    data = "Hello, world!"
    data = data.encode("utf8")
    socket.sendall(data)
    
except:
    print("connection serveur failed")
    socket.close()
finally:
    socket.close()