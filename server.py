#jessica Brown
#socket assignment. this is the server part
#it is in python

from socket import *
from datetime import datetime #could be needed
serverPort = 8300

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
print("the server is ready to recive")

while True:
#    connectionSocket, addr = serverSocket.accept()
    message, clientAddress = serverSocket.recvfrom(2048)
    print(message)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode().clientAddress)
if True:
    print("OK")
else:
    print("INVALID TRY AGAIN")

#set port
if port != 8000:
    serverPort=port
else:
    serverPort=8000
    
#IP method handling
if requestMethod == 'IP':
    logRequest(requestMethod,okCode)
    returnMessage = okCode+'_' + clientAddress[IPindex]

#PORT method handling
elif requestMethod == 'PORT':
    logRequest(requestMethod,okCode)
    returnMessage = okCode+'_'+ str(clientAddress[portIndex])
    return returnMessage
