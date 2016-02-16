#!/usr/bin/python

import socket
import random

host = socket.gethostname()
port = 1235

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

mySocket.bind((host, port))

mySocket.listen(5)

try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'Request received:'
        print recvSocket.recv(2048)
        print 'Answering back...'
        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body>" +
                        "<p>Pincha aqui: </p>" +
                        "<a href=http://" +
                        host +
                        ":" +
                        str(port) + 
                        "/" +
                        str(random.randint(1, 10)) +
                        ">enlace</a>" +
                        "</body></html>" +
                        "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    mySocket.close("Closing binded socket")
