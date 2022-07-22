import socket
from struct import pack
from tabnanny import check

HOST = "127.0.0.1"
PORT = 65432


def menu():
    print("--------------------------------------")
    print("Sistema de Email Liame.")
    print("Digite 1 para ENTRAR.")
    print("Digite 2 para REGISTRAR.")
    print("Digite 3 para ENVIAR MENSAGEM.")
    print("Digite 4 para VER MENSAGENS.")
    print("Digite 5 para APAGAR MENSAGENS.")
    print("Digite 0 para SAIR.")
    print("--------------------------------------")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mail_system:
    mail_system.connect((HOST, PORT))
    menu()
    while True:
        option = str(input("O que deseja fazer:"))
        if option == '1':
            email = str(input("Seu e-mail: "))
            password = str(input("Sua senha: "))
            message = f'{1}-{email};{password}'
            mail_system.send(str.encode(message))

            comfirm = mail_system.recv(1024).decode()
            print(comfirm)

        elif option == '2':
            name = str(input("Seu nome: "))
            email = str(input("Seu nome de e-mail: ")) + "@liame.com"
            password = str(input("Sua senha: "))
            message = f'{2}-{name};{email};{password}'
            mail_system.send(str.encode(message))

            comfirm = mail_system.recv(1024).decode()
            print(comfirm)

        elif option == '3':
            mailTo = str(input("Digite o e-mail de destino: "))
            subject = str(input("Digite o assunto do e-mail: "))
            message = str(input("Digite a mensagem do e-mail: "))
            package = f'{3}-{mailTo};{subject};{message}'
            mail_system.send(str.encode(package))

            comfirm = mail_system.recv(1024).decode()
            print(comfirm)

        elif option == '4':
            package = f'{4}-sb'
            mail_system.send(str.encode(package))
            mailBox = mail_system.recv(1024).decode()

            mails = mailBox.split('-')
            mails.pop()

            index = 0
            for mail in mails:
                detailsMail = mail.split(';')
                print('\nIndex: ' + str(index) + '\nDe: ' + detailsMail[0] + '\nAssunto: ' +
                      detailsMail[1] + '\nMensagem: ' + detailsMail[2] + '\n')
                index += 1

        elif option == '5':
            index = input("Digite o indice da mensagem que deseja apagar: ")
            package = f'{5}-{index}'
            mail_system.send(str.encode(package))

            comfirm = mail_system.recv(1024).decode()
            print(comfirm)

        elif option == '0':
            package = f'{0}-c'
            mail_system.send(str.encode(package))
            mail_system.close()
            print("Conexão Encerrada.")
            break
