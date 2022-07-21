import socket
from accounts import Liame

HOST = "127.0.0.1"
PORT = 65432

functions = Liame()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as email_server:
    email_server.bind((HOST, PORT))
    email_server.listen()
    print(f"Porta: {PORT}")
    conn, addr = email_server.accept()

    with conn:
        print(f"Conectado: {addr}")
        while True:
            option = conn.recv(1024)
            if option == '0':
                print('cheguei aqui!')
                conn.send(functions.signin())
            elif option == 1:
                functions.login()
            elif option == 2:
                functions.sendMessage()
            elif option == 3:
                functions.showBoxMail()
            elif option == 4:
                functions.openMessage()
            elif option == 5:
                functions.deleteMessage()
            elif option == 6:
                email_server.close()
                break

            # data = conn.recv(1024)
            # print(data.decode())
            # if not data:
            #     break
            # conn.sendall(data)
        email_server.close()
        print("Conexão Encerrada.")

