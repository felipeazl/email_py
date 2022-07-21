import os
from tkinter import *
from tkinter import font
from turtle import width


def saveSignin(name, email, password):
    userRegister = open('userRegister.txt','a')
    userRegister.write('\nName: ' + name)
    userRegister.write('\nE-mail: ' + email)
    userRegister.write('\nPassword: ' + password)
    userRegister.write("\n\n")
    userRegister.close()

# saveSignin('Alipio', 'alipio@emai.com', '1234456')

def saveOnMyBoxEmail(email, message):
    boxEmail = open('boxEmail-'+ email, 'a')
    boxEmail.write('\nFrom: ' + message['from'])
    boxEmail.write('\nSubject: ' + message['subject'])
    boxEmail.write('\nMessage: ' + message['message'])
    boxEmail.write("\n")
    boxEmail.close()

# saveOnMyBoxEmail('duda@email.com',{'from':'alipio@email', 'subject':'Assunto teste 2', 'message': 'Oi duda, e um teste'})
# saveOnMyBoxEmail('duda@email.com',{'from':'alipio@email', 'subject':'Assunto teste 123456', 'message': 'Oi duda, e um teste'})
# saveOnMyBoxEmail('alipio@email.com',{'from':'duda@email', 'subject':'Assunto teste blabla', 'message': 'Oi alipio, e um teste'})



# ### Alipio
# c = os.path.dirname(__file__)
# infos = c+"\\Registros.txt"

# def testezinho():
#     arquivo=open(infos,"a")
#     arquivo.write("\nNome....: %s" % vt1.get())
#     arquivo.write("\nE-mail..: %s" % vt2.get())
#     arquivo.write("\nSenha...: %s" % vt3.get())
#     arquivo.write("\n")
#     arquivo.close()

# app=Tk()
# app.title("\nEFETUE SEU REGISTRO:")
# app.geometry("320x205")
# app.configure(background="#142559")

# Label(app, text="Nome:",background="#142559",foreground="#ffffff",anchor=W,font="Roboto 10 bold").place(x=10,y=10,width=70,height=20)
# vt1=Entry(app)
# vt1.place(x=10,y=30,width=300,height=20)

# Label(app, text="Seu e-mail:",background="#142559",foreground="#ffffff",anchor=W,font="Roboto 10 bold").place(x=10,y=60,width=100,height=20)
# vt2=Entry(app)
# vt2.place(x=10,y=80,width=300,height=20)

# Label(app, text="Sua senha:",background="#142559",foreground="#ffffff",anchor=W,font="Roboto 10 bold").place(x=10,y=110,width=200,height=20)
# vt3=Entry(app)
# vt3.place(x=10,y=130,width=300,height=20)

# Button(app,text="Confirma",command=testezinho,anchor=W,font="Roboto 10 bold").place(x=10,y=170,width=70,height=20)

# app.mainloop() 
