from socket import *
import threading
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive.")

def service_function(connection_socket):
    while True:
        sentence = connection_socket.recv(1024).decode()
        if sentence == "Quit":
            connection_socket.close()
            break
        else:
            connection_socket.send(sentence.upper().encode())

class ServiceThread(threading.Thread):
    def __init__(self, connection_socket):
        threading.Thread.__init__(self)
        self.connection_socket = connection_socket
        
    def run(self):
        service_function(self.connection_socket)

while True:
    connection_socket, addr = serverSocket.accept()
    new_thread = ServiceThread(connection_socket)
    new_thread.start()