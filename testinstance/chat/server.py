import socket

msocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
msocket.bind(('',18677))
msocket.listen(5)

while True:
    connection,addr = msocket.accept()
    revStr = connection.recv(1024)
    connection.send('server:'+revStr)
    connection.close()
