import os
from tkinter import *
from tkinter import font
from turtle import width


# função para salvar os usuários registrados em um arquivo
def saveSignin(name, email, password):
    # abre o aquivo, e insere as informações do novo usuário registrado
    userRegister = open('userRegister.txt', 'a')
    userRegister.write(name+';'+email+';'+password+'-')
    userRegister.close()
    # cria uma caixa de e-mail para o novo usuário
    boxEmail = open('emails/boxEmail-' + email + '.txt', 'a')
    boxEmail.close()


# função que salva as mensagens recebidas na caixa de e-mail do usuário que recebeu as mensagens
def saveOnMyBoxEmail(email, mailFrom, subject, message):
    # abre o aquivo e insere as informações do e-mail recebido
    boxEmail = open('emails/boxEmail-' + mailFrom + '.txt', 'a')
    boxEmail.write(email+';'+subject+';'+message+'-')
    boxEmail.close()


# função que verifica se o e-mail já foi registrado ou não. Retorna verdadeiro ou falso
def verifyEmail(email):
    archive = open('userRegister.txt', 'r')
    # todos os dados registrados de todos os usuários
    readArchive = archive.read()
    # divide em cada usuário
    userData = readArchive.split("-")
    userData.pop()

    # loop para percorrer todos os usuário cadastrados
    for user in userData:
        # para cada usuário, divide as duas informações (ex: divide nome do e-mail e da senha)
        informationUser = user.split(';')
        # information[0] = nome ; information[1] = email ; information[2] = senha
        if informationUser[1] == email:
            return True
    return False


# função que lê a caixa de e-mail de um usuário e a retorna.
def showBoxMessage(email):
    archive = open('emails/boxEmail-' + email + '.txt', 'r')
    readArchive = archive.read()
    return readArchive


# função que verifica se as informações de login que o usuário inseriu, batem com um usuário já registrado
def login(email, password):
    # abre o aquivo para leitura
    archive = open('userRegister.txt', 'r')
    # todos os dados registrados de todos os usuários
    readArchive = archive.read()
    # divide em cada usuário
    userData = readArchive.split("-")

    # loop para percorrer todos os usuário cadastrados
    for user in userData:
        # para cada usuário, divide as duas informações (ex: divide nome do e-mail e da senha)
        informationUser = user.split(';')
        # information[0] = nome ; information[1] = email ; information[2] = senha
        if informationUser[1] == email and informationUser[2] == password:
            archive.close()
            # retorna o e-mail do usuário que está logado no sistema para o servidor
            return informationUser[1]
    archive.close()
    return False


# função que deleta uma mensagem da caixa de e-mail do usuário logado
def deleteMessage(email, index):
    # abre o aquivo para leitura
    archive = open('emails/boxEmail-' + email + '.txt', 'r')
    readArchive = archive.read()
    # divide a caixa de e-mail em cada mensagem recebida
    mails = readArchive.split('-')
    # deleta a última mensagem, pois ela sempre é em branco por padrão do desenvolvimento
    mails.pop()
    # deleta a mensagem escolhida
    mails.pop(int(index))

    # abre o arquivo da caixa de email do usuário logado, para subescrever
    rewrite = open('emails/boxEmail-' + email + '.txt', 'w')
    # loop que percorre cada email da lista dos mesmos
    for mail in mails:
        # sobescreve o arquivo caixa de e-mail, com os e-mails que ainda devem permanecer na mesma
        rewrite.write(str(mail) + '-')
    archive.close()
    rewrite.close()
