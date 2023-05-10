import socket
hostname = socket.gethostname()
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input("Input lowercase sentence:")
clientSocket.sendto(message.encode('UTF-8'),('', serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()


