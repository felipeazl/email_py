#Objeto para caixa de e-mail

class EmailAccounts:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email + "@liame.com"
        self.password = password
        self.boxMessage = []

class Liame:

    def __init__(self):
        self.registeredUsers = []
        self.loggedUser = ""
        
    def signin(self):
        name = str(input("Seu nome: "))
        email = str(input("Seu e-mail: "))
        password = str(input("Sua senha: "))

        for user in self.registeredUsers:
            # percorre todos os e-mails cadastrados e verifica se é igual ao email inserido.
            if user.email == email + "@liame.com":
                print("e-mail já cadastrado, chame a função novamente e insira um e-mail que ainda não foi cadastrado.")

        user = EmailAccounts(name, email, password)
        self.registeredUsers.append(user)

        print("User cadastrado!", user.email)

    def login(self):
        email = str(input("Seu e-mail: "))
        password = str(input("Sua senha: "))

        for user in self.registeredUsers:
            #verificação se o e-mail inserido é igual a de um usuário cadastrado
            if user.email == email:
                #Verificando se a senha é igual a do usuário cadastrado
                if user.password == password:
                    self.loggedUser = user
                    print("usuário logado!")
                else:
                    print("senha invalida")

    def sendMessage(self):

        if self.loggedUser == "":
            print("Usuário não logado, por favor faça login para enviar uma mensagem")

        else:
            mailTo = str(input("Digite o e-mail de destino: "))
            subject = str(input("Digite o assunto do e-mail: "))
            message = str(input("Digite a mensagem do e-mail: "))

            #empacotamento do e-mail
            email = {'from': self.loggedUser.email, 'subject': subject, 'message': message}

            #percorre todos os usuários registrados
            for user in self.registeredUsers:
                #verifica se o e-mail existe
                if user.email == mailTo:
                    #se existe adiciona o e-mail na caixa de e-mail do usuário
                    user.boxMessage.append(email)
                    print("e-mail enviado!")

    
    def showBoxMail(self):
        if self.loggedUser == "":
            print("Usuário não logado, por favor faça login para enviar uma mensagem")

        else:
            for boxes in self.loggedUser.boxMessage:
                print(boxes)

    def openMessage(self):
        if self.loggedUser == "":
            print("Usuário não logado, por favor faça login para abrir uma mensagem")

        else:
            messageIndex = int(input("Digite o indice da mensagem que deseja visualizar: "))
            print(self.loggedUser.boxMessage[messageIndex].message)

    def deleteMessage(self):
        if self.loggedUser == "":
            print("Usuário não logado, por favor faça login para deletar uma mensagem")

        else:
            messageIndex = int(input("Digite o indice da mensagem que deseja apagar: "))
            self.loggedUser.boxMessage.pop(messageIndex)

liame = Liame()
liame.signin()
liame.signin()
liame.signin()
liame.login()
liame.sendMessage()
liame.login()
liame.showBoxMail()
liame.openMessage()
liame.deleteMessage()
liame.showBoxMail()