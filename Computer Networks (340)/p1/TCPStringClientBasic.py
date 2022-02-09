from socket import *

serverName = 'localhost'
serverPort = 5000
while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    requestString = input("Input a sentence: ")
    if requestString == "quit":
        break
    else:
        clientSocket.send(requestString.encode())
        response = clientSocket.recv(1024)
        print(response.decode())
clientSocket.close()

