import socket
# hostname = socket.gethostname()
hostname = "127.0.0.1"
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((hostname, serverPort))
translator = {"abelha":"bee",
              "banana":"banana",
              "casa":"house",
              "dado":"dice",
              "estrada":"street",
              "faca":"knife",
              "gato":"cat",
              "humano":"human",
              "inteligencia":"inteligece",
              "jabuti":"tortoise"}
print(hostname)
print("----------The server is ready to receive----------")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode('UTF-8')
    translated = translator[modifiedMessage].encode('UTF-8')
    serverSocket.sendto(translated, clientAddress)
    print(modifiedMessage)
