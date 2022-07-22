import os
from tkinter import *
from tkinter import font
from turtle import width


def saveSignin(name, email, password):
    userRegister = open('userRegister.txt', 'a')
    userRegister.write(name+';'+email+';'+password+'-')
    userRegister.close()
    boxEmail = open('emails/boxEmail-' + email + '.txt', 'a')
    boxEmail.close()


def saveOnMyBoxEmail(email, mailFrom, subject, message):
    boxEmail = open('emails/boxEmail-' + mailFrom + '.txt', 'a')
    boxEmail.write(email+';'+subject+';'+message+'-')
    boxEmail.close()


def verifyEmail(email):
    archive = open('userRegister.txt', 'r')
    readArchive = archive.read()  # todos os dados registrados de todos os usuários
    # lista com data elemento sendo um pacote com as 3 informações dos usuários
    userData = readArchive.split("-")
    userData.pop()

    for user in userData:
        informationUser = user.split(';')
        if informationUser[1] == email:
            return True
    return False


def showBoxMessage(email):
    archive = open('emails/boxEmail-' + email + '.txt', 'r')
    readArchive = archive.read()
    return readArchive


def login(email, password):
    archive = open('userRegister.txt', 'r')
    readArchive = archive.read()  # todos os dados registrados de todos os usuários
    # lista com data elemento sendo um pacote com as 3 informações dos usuários
    userData = readArchive.split("-")

    for user in userData:
        informationUser = user.split(';')
        if informationUser[1] == email and informationUser[2] == password:
            archive.close()
            return informationUser[1]
    archive.close()
    return False


def deleteMessage(email, index):
    archive = open('emails/boxEmail-' + email + '.txt', 'r')
    readArchive = archive.read()

    print("caixa de email: ", readArchive)

    mails = readArchive.split('-')
    mails.pop()
    mails.pop(int(index))

    rewrite = open('emails/boxEmail-' + email + '.txt', 'w')
    for mail in mails:
        rewrite.write(str(mail) + '-')

    archive.close()
    rewrite.close()
