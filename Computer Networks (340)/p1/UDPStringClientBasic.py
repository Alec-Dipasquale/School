from socket import *

serverName = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    requestString = input("Input a sentence: ")
    if requestString == "quit":
        break
    else:
        clientSocket.sendto(requestString.encode(), (serverName, serverPort))
        responseString, serverAddress = clientSocket.recvfrom(1024)
        print(responseString.decode())
clientSocket.close()
