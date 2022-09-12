#jessica Brown
#socket assignment. this is the client end
#this is in python and doesn't work


from socket import *
serverName = '127.0.0.1'
serverport = 8300
clientSocket= socket(AF_INET, SOCK_DGRAM)

message = imput ('Input lowercase sentence: ')
clientSocket.sentto(message.encode(),(serverName,serverPort))

modifiedMessage, serverAddress = clientSocet.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close
