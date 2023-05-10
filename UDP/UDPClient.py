import socket
# hostname = socket.gethostname()
hostname = "127.0.0.1"
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = ["abelha","banana","casa","dado","estrada","faca","gato","humano","inteligencia","jabuti"]
messageencode = [x.encode('utf-8') for x in message]
listaModificada = []
print("----------Mensagens enviadas pelo cliente:----------")
for i in messageencode:
    print(i)
    clientSocket.sendto(i,(hostname, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    listaModificada.append(modifiedMessage.decode('UTF-8'))
print("----------Mensagens recebidas pelo cliente:----------")
for i in listaModificada:
    print(i)
clientSocket.close()


