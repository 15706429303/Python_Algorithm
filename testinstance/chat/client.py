import socket
import time

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsocket.connect(('',18677))
while True:
    time.sleep(2)
    clientsocket.send('hello the5fire')
    print clientsocket.recv(2014)

clientsocket.close()