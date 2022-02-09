from socket import *
import threading
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive.")
while True:
    connectionSocket, addr = serverSocket.accept()
    while True:
        sentence = connectionSocket.recv(1024).decode()
        if sentence == "Quit":
            print("Done with one client.")
            connectionSocket.close()
            break
        else:
            capitalizedSentence = sentence.upper()
            connectionSocket.send(capitalizedSentence.encode())