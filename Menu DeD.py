from tkinter import *
from personagem import buscar_personagem
import listboxDeD
import BancoDeD

menu = Tk()
menu.geometry("750x575")
menu.title("Menu da criação de ficha")
BancoDeD.banco()

#  MENU
introducao = Label(menu, text="Bem-Vindo a criação de fichas D&D 5e !! ", bg="grey")
introducao.pack(side=TOP, fill=X)

#  USUARIOS

usuario = Label(menu, text="Registre um Usuário: ")
usuario.place(x=0, y=25)

nome_ed = Entry(menu, width=59)
nome_ed.place(x=117, y=25)

usuario = Label(menu, text="Apagar um Usuário: ")
usuario.place(x=0, y=60)

nome_ed2 = Entry(menu, width=59)
nome_ed2.place(x=117, y=60)

usuario = Label(menu, text="Consulte um Usuário: ")
usuario.place(x=0, y=100)

nome_ed3 = Entry(menu, width=59)
nome_ed3.place(x=117, y=100)

usuario = Label(menu, text="Atualize um Usuário: ")
usuario.place(x=0, y=140)

nome_ed4 = Entry(menu, width=59)
nome_ed4.place(x=117, y=140)

def pegandod():
    nome1 = nome_ed.get()
    BancoDeD.cadastrar_u(nome1)

buscar = Listbox(menu, width=115, height=22)
buscar.place(x=20, y=180)

listboxDeD.buscar_u(buscar)

confirmar1 = Button(menu, width=15, text="Registrar", command=pegandod)
confirmar1.place(x=600 ,y=22)

confirmar2 = Button(menu, width=15, text="Pesquisar", command=buscar_personagem)
confirmar2.place(x=600 ,y=95)

def pegandod2():
    nome1 = nome_ed2.get()
    BancoDeD.apagar_u(nome1)

confirmar3 = Button(menu, width=15, text="Apagar", command=pegandod2)
confirmar3.place(x=600 ,y=58)

def atualizando():

    atualizar = Tk()
    atualizar.geometry("450x120")
    atualizar.title("Atualizando um Usuário")

    usuario = Label(atualizar ,text="Digite o Novo Nome de Usuário: ")
    usuario.place(x=0, y=0)

    nome_ed3 = Entry(atualizar, width=40)
    nome_ed3.place(x=190, y=0)

    def pegandod3():
        nome1, nome2 = nome_ed3.get(), nome_ed4.get()
        BancoDeD.atualizar_u(nome1,nome2)

    confirmar4 = Button(atualizar, width=15, text="Confirmar", command=pegandod3)
    confirmar4.place(x=170,y=50)

confirmar5 = Button(menu, width=15, text="Atualizar", command=atualizando)
confirmar5.place(x=600 ,y=135)

voltar = Button(menu,width=30, text="Sair do Sistema", command=menu.destroy)
voltar.pack(side=BOTTOM)

menu.mainloop()

    
