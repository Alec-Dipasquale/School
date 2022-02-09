from socket import *
import threading

serverName = 'localhost'
serverPort = 5000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    sentence = input("Input a lowercase sentence: ")
    clientSocket.send(sentence.encode())
    if sentence == "Quit":
        break
    else:
        modifiedSentence = clientSocket.recv(1024)
        print(modifiedSentence.decode())

clientSocket.close()