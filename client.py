import socket
from accounts import Liame

HOST = "127.0.0.1"
PORT = 65432
DOMAIN = "@liame.com"


# def menu():
#     print("Sistema de Email Liame.")
#     print("Digite o número correspondente a cada funçõa que deseja utilizar.")
#     print("0 = Registrar\n1 = Entrar\n2 = Enviar Mensagem\n3 = Ver Caixa de Mensagens\n4 = Abrir Mensagem\n5 = Deletar Mensagem\n6 = Encerrar Programa")


functions = Liame()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mail_system:
    mail_system.connect((HOST, PORT))
    teste = str(input())
    mail_system.sendall(str.encode(teste))
    # menu()
    # while True:
    #     select_menu = int(input("Digite o que você deseja fazer: "))
    #     if select_menu == 0:
    #         functions.signin()
    #     elif select_menu == 1:
    #         functions.login()
    #     elif select_menu == 2:
    #         functions.sendMessage()
    #     elif select_menu == 3:
    #         functions.showBoxMail()
    #     elif select_menu == 4:
    #         functions.openMessage()
    #     elif select_menu == 5:
    #         functions.deleteMessage()
    #     elif select_menu == 6:
    #         mail_system.close()
    #         break
