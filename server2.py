#jessica Brown
#socket assignment. this is the 2nd server end
#this is in python and doesn't work  

from socket import *
serverPort = 8300

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("The server is ready to recive")


while true:
    connectionSocket, addr = serverSocket.accept()
