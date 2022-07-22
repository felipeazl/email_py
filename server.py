import socket  # importa biblioteca socket
from functions import *  # importa as funções criadas para o sistema

HOST = "127.0.0.1"  # endereço padrão do localhost
PORT = 65432  # porta padrão
userLoged = False  # define que o usuário inicia sempre deslogado

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mail_server:
    # inicia o servidor com o endereço e portas já definidos
    mail_server.bind((HOST, PORT))
    mail_server.listen()  # aguarda conexão
    print(f"Porta: {PORT}")
    conn, addr = mail_server.accept()  # aceita conexão

    # quando conectado, mostra o endereço do cliente conectado e inicia o funcionamento.
    with conn:
        print(f"Conectado: {addr}")
        while True:
            # recebe um pacote do cliente, onde o primeiro elemento é o código que indica qual ação o usuário deseja realizar e o segundo elemento são as demais informações necessarias para executar a ação
            package = conn.recv(1024).decode()
            # divide o pacote em dois: o código da ação e as informações
            data = package.split('-')
            # data[0] = option ; data[1] = informações necessárias dividas por ';'
            option = data[0]

            # opção 1 - Entrar no Sistema
            if option == '1':
                # divide as informações necessárias
                message = data[1].split(';')
                #message[0] = email ; message[1] = senha
                # Chama a função de login do arquivo functions e armazena o e-mail do usuário logado em userLoged
                userLoged = login(message[0], message[1])
                # retorna mensagem de sucesso
                conn.send(str.encode('Usuário logado com sucesso'))

            #  opção 2 - Registrar
            elif option == '2':
                # divide as informações necessárias
                message = data[1].split(';')
                #message[0] = nome ; message[1] = email ; message[2] = senha
                # Chama a função de saveSignin do arquivo functions
                saveSignin(message[0], message[1], message[2])
                # retorna mensagem de sucesso
                conn.send(str.encode('Usuário cadastrado!'))

            # opção 3 - Enviar Mensagem
            elif option == '3':
                # verifica se o usuário não esta logado
                if not userLoged:
                    # retorna mensagem de erro
                    conn.send(str.encode('Usuário Não logado'))
                else:
                    # divide as informações necessárias
                    message = data[1].split(';')
                    # message[0] = Para e-mail ; message[1] = assunto do e-mail ; message[2] = mensagem do e-mail
                    if verifyEmail(message[0]):
                        # Chama a função de saveOnMyBoxEmail do arquivo functions
                        saveOnMyBoxEmail(
                            userLoged, message[0], message[1], message[2])
                        # retorna mensagem de sucesso
                        conn.send(str.encode('Mensagem enviada com sucesso!'))
                    else:
                        # retorna mensagem de erro
                        conn.send(str.encode(
                            'E-mail não existe, insira um e-mail válido'))

            # opção 4 - Ver Mensagens
            elif option == '4':
                # verifica se o usuário não esta logado
                if not userLoged:
                    # retorna mensagem de erro
                    conn.send(str.encode('Usuário Não logado'))
                else:
                    # Chama a função de showBoxMessage do arquivo functions
                    boxMessage = showBoxMessage(userLoged)
                    # retorna a caixa de e-mail
                    conn.send(str.encode(boxMessage))

            # opção 5 - Apagar Mensagem
            elif option == '5':
                # verifica se o usuário não esta logado
                if not userLoged:
                    # retorna mensagem de erro
                    conn.send(str.encode('Usuário Não logado'))
                else:
                    # Chama a função de deleteMessage do arquivo functions
                    deleteMessage(userLoged, data[1])
                    # retorna mensagem de sucesso
                    conn.send(str.encode('Mensagem deletada'))

            # opção 0 - Encerrar Conexão
            elif option == '0':
                # para o loop
                break

    # Encerra a conecção pela parte do servidor
    mail_server.close()
    print("Conexão Encerrada.")
