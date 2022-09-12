#jessica Brown
#socket assignment. this is the server part
#it is in pythony

from socket import *
serverPort = 8300

serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("the server is ready to recive")

while true:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(message)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode().clientAddress)
