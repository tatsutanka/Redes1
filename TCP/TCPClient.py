import socket
# hostname = socket.gethostname()
hostname = "127.0.0.1"
serverPort = 12000
message = ["abelha",
           "banana",
           "casa",
           "dado",
           "estrada",
           "faca",
           "gato",
           "humano",
           "inteligencia",
           "jabuti"]
messageencode = [x.encode('utf-8') for x in message]
returnListModified = []

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((hostname,serverPort))
print("----------Mensagens enviadas pelo cliente:----------")
for i in messageencode:
    print(i)
    clientSocket.send(i)
    modifiedMessage = clientSocket.recv(2048)
    returnListModified.append(modifiedMessage.decode('UTF-8'))
print("----------Mensagens recebidas pelo cliente:----------")
for i in returnListModified:
    print(i)
clientSocket.close()



