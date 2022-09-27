#jessica Brown
#socket assignment. this is the client end
#this is in python and doesn't work


from socket import *
from datetime import datetime #could be needed
serverName = '127.0.0.1'
serverPort = 8300
clientSocket= socket(AF_INET, SOCK_DGRAM)

message = input ('Input lowercase sentence: ')
clientSocket.sendto(message.encode(),(serverName,serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close
