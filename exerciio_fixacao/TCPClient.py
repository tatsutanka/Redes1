import socket 
hostname = socket.gethostname()
serverPort = 12000
clienSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clienSocket.connect((hostname,serverPort))
sentence = input("Lower case sentence:")
clienSocket.send(sentence.encode('UTF-8'))
modifiedSencentence = clienSocket.recv(1024)
print("From Server:",modifiedSencentence)
clienSocket.close()
