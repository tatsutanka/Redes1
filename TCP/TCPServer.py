import socket
# hostname = socket.gethostname()
hostname = "127.0.0.1"
serverPort = 12000
translator = {"abelha":"bee",
              "banana":"banana",
              "casa":"house",
              "dado":"dice",
              "estrada":"street",
              "faca":"knife",
              "gato":"cat",
              "humano":"human",
              "inteligencia":"inteligece",
              "jabuti":"tortoise",
              }
print(hostname)
print("----------The server is ready to receive----------")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((hostname,serverPort))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print("Conectado:",addr)
        while True:
            message = conn.recv(2048)
            if not message:
                break
            modifiedMessage = message.decode('UTF-8')
            translated = translator[modifiedMessage].encode('UTF-8')
            conn.send(translated)
            print(modifiedMessage)
