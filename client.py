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

#processes response from server
def processReponse(selection, modifiedMessage):
    currentTime = datetime.now().timestamp()
    
    if selection != 3:
        print(modifiedMessage.decode())
    else:
        #calculation of return time from server
        returnMessage=modifiedMessage.decode().split('_')
        returnTime=currentTime-float(returnMessage[3])

    print('Server date and time: '+returnMessage[1]+'\nTime from client to server: '+returnMessage[2]+'\nTime from server to client: '+str(returnTime))
    clientSocket.close()
    #sets port
    if port != 8000:
        serverPort=port
    else:
        serverPort=8000
        
    #sets IP
    if ip != '127.0.0.1':
        serverName=ip
    else:
        serverName='127.0.0.1'
        
