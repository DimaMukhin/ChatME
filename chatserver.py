import socket
import time
import threading

bind_ip = '192.168.1.2'
bind_port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
clients = []

print 'Listening on {}:{}'.format(bind_ip, bind_port)

def handleClientConnection(client_socket, address):
    run = True
    while run:
        try:
            request = client_socket.recv(1024)
            if request:
                print time.ctime(time.time()) + str(address) + ' :' + str(request)
                for client in clients:
                    client.send(str(request))
        except Exception as e:
            clients.remove(client_socket)
            run = False

while True:
    client_sock, address = server.accept()
    clients.append(client_sock)
    print 'Accepted connection from {}:{}'.format(address[0], address[1])
    client_handler = threading.Thread(
        target=handleClientConnection,
        args=(client_sock, address[0])
    )
    client_handler.start()
