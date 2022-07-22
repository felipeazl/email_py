import socket
from functions import *

HOST = "127.0.0.1"
PORT = 65432
userLoged = False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mail_server:
    mail_server.bind((HOST, PORT))
    mail_server.listen()
    print(f"Porta: {PORT}")
    conn, addr = mail_server.accept()

    with conn:
        print(f"Conectado: {addr}")
        while True:
            package = conn.recv(1024).decode()
            print(package)
            data = package.split('-')

            print(data)
            option = data[0]

            if option == '1':
                message = data[1].split(';')
                userLoged = login(message[0], message[1])
                conn.send(str.encode('Usuário logado com sucesso'))
            elif option == '2':
                message = data[1].split(';')
                saveSignin(message[0], message[1], message[2])
                conn.send(str.encode('Usuário cadastrado!'))
            elif option == '3':
                if not userLoged:
                    conn.send(str.encode('Usuário Não logado'))
                else:
                    message = data[1].split(';')
                    if verifyEmail(message[0]):
                        saveOnMyBoxEmail(
                            userLoged, message[0], message[1], message[2])
                        conn.send(str.encode('Mensagem enviada com sucesso!'))
                    else:
                        conn.send(str.encode(
                            'E-mail não existe, insira um e-mail válido'))
            elif option == '4':
                if not userLoged:
                    conn.send(str.encode('Usuário Não logado'))
                else:
                    boxMessage = showBoxMessage(userLoged)
                    conn.send(str.encode(boxMessage))
            elif option == '5':
                if not userLoged:
                    conn.send(str.encode('Usuário Não logado'))
                else:
                    deleteMessage(userLoged, data[1])
                    conn.send(str.encode('Mensagem deletada'))

            elif option == '0':
                break

    mail_server.close()
    print("Conexão Encerrada.")
