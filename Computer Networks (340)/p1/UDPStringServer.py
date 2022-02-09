from socket import *

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The UDP server is ready.")
while True:
    request, clientAddress = serverSocket.recvfrom(2048)
    responseString = request.decode().upper()
    print("Message to be sent back to the client: ")
    print(responseString)
    serverSocket.sendto(responseString.encode(), clientAddress)
