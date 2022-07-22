import socket  # importa a biblioteca socket

# endereço e porta dos servidores que iremos realizar a conexão.
HOST = "127.0.0.1"
PORT = 65432


def menu():  # função para exibir o menu de opções que o usuário podera fazer.
    print("--------------------------------------")
    print("Sistema de Email Liame.")
    print("Digite 1 para ENTRAR.")
    print("Digite 2 para REGISTRAR.")
    print("Digite 3 para ENVIAR MENSAGEM.")
    print("Digite 4 para VER MENSAGENS.")
    print("Digite 5 para APAGAR MENSAGENS.")
    print("Digite 0 para SAIR.")
    print("--------------------------------------")


# realiza a conexão com o servidor, através de seu endereço e sua porta.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mail_system:
    mail_system.connect((HOST, PORT))
    menu()
    while True:
        # input para usuário selecionar o que deseja fazer
        option = str(input("O que deseja fazer:"))
        # opção 1 - Entrar no Sistema
        if option == '1':
            # usuário entra com seu email e senha.
            email = str(input("Seu e-mail: "))
            password = str(input("Sua senha: "))
            # dados são "empacotados" para serem enviados ao servidor
            message = f'{1}-{email};{password}'
            # envia os dados codificados para o servidor
            mail_system.send(str.encode(message))

            # recebe, decodifica e exibe para o usuário uma confirmação do servidor de que a operação realizada
            comfirm = mail_system.recv(1024).decode()
            print(comfirm)

        #  opção 2 - Registrar
        elif option == '2':
            # usuário digita o seu nome, email e senha para depois poder acessar o sistema
            name = str(input("Seu nome: "))
            # digita somente o username do email, o dominio é completado automaticamente
            email = str(
                input("Seu nome de e-mail(sem o dominio): ")) + "@liame.com"
            password = str(input("Sua senha: "))
            # dados são "empacotados" para serem enviados ao servidor
            message = f'{2}-{name};{email};{password}'
            # envia os dados codificados para o servidor
            mail_system.send(str.encode(message))

            # recebe, decodifica e exibe para o usuário uma confirmação do servidor de que a operação realizada
            comfirm = mail_system.recv(1024).decode()
            print(comfirm)

        # opção 3 - Enviar Mensagem
        elif option == '3':
            # recebe o email de destino, o assunto da mensagem e a mensagem
            mailTo = str(input("Digite o e-mail de destino: "))
            subject = str(input("Digite o assunto do e-mail: "))
            message = str(input("Digite a mensagem do e-mail: "))
            # dados são "empacotados" para serem enviados ao servidor
            package = f'{3}-{mailTo};{subject};{message}'
            # envia os dados codificados para o servidor
            mail_system.send(str.encode(package))

            # recebe, decodifica e exibe para o usuário uma confirmação do servidor de que a operação realizada
            comfirm = mail_system.recv(1024).decode()
            print(comfirm)

        # opção 4 - Ver Mensagens
        elif option == '4':
            # dados são "empacotados" para serem enviados ao servidor
            package = f'{4}-sb'
            # envia os dados codificados para o servidor
            mail_system.send(str.encode(package))
            # recebe as mensagens do servidor para exibir para o usuário
            mailBox = mail_system.recv(1024).decode()

            # realiza a função split nos separadores para dividir as mensagens
            mails = mailBox.split('-')
            mails.pop()  # apaga a ultima mensagem que sempre é uma mensagem vazia

            index = 0
            # formata a mensagem para uma exibição mais agradavel
            for mail in mails:  # percorre todas as mesagens
                # divide os dados de cada mensgem
                detailsMail = mail.split(';')
                # monta a mensagem que será exibida para o usuário
                print('\nIndex: ' + str(index) + '\nDe: ' + detailsMail[0] + '\nAssunto: ' +
                      detailsMail[1] + '\nMensagem: ' + detailsMail[2] + '\n')
                index += 1

        # opção 5 - Apagar Mensagem
        elif option == '5':
            # recebe como parametro somente o index da mensagem que deseja ser apagada.
            index = input("Digite o indice da mensagem que deseja apagar: ")
            # dados são "empacotados" para serem enviados ao servidor
            package = f'{5}-{index}'
            # envia os dados codificados para o servidor
            mail_system.send(str.encode(package))

            # recebe, decodifica e exibe para o usuário uma confirmação do servidor de que a operação realizada
            comfirm = mail_system.recv(1024).decode()
            print(comfirm)

        # opção 0 - Encerrar Conexão
        elif option == '0':
            # dados são "empacotados" para serem enviados ao servidor
            package = f'{0}-c'
            # envia os dados codificados para o servidor
            mail_system.send(str.encode(package))

            # fecha a conexão com o servidor e alerta para usuário
            mail_system.close()
            print("Conexão Encerrada.")
            break
