from socket import *

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The TCP server is ready.")
while True:
    connectionSocket, addr = serverSocket.accept()
    requestString = connectionSocket.recv(1024).decode()
    responseString = requestString.upper()
    print("Message to be sent back to client: ")
    print(responseString)
    connectionSocket.send(responseString.encode())
    connectionSocket.close()
