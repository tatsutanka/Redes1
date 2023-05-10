import socket
hostname = socket.gethostname()
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Pode mandar")
while 1:
    conectionSocket, addr = serverSocket.accept()
    sentence = conectionSocket.recv(1024)
    captalziedSentence = sentence.decode('UTF-8')
    conectionSocket.send(captalziedSentence.encode('UTF-8'))
    print(sentence)
    conectionSocket.close()
