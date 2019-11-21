from tkinter import *
import listboxDeD
import tkinter.ttk as ttk
import BancoDeD

def buscar_personagem():

    personagem = Tk()
    personagem.geometry("850x648")
    personagem.title("Escolha seu Personagem")
    
    nome_p = Label(personagem, text="Digite o nome do seu personagem: ")
    nome_p.place(x=0, y=0)

    nome_p_ed = Entry(personagem, width=59)
    nome_p_ed.place(x=195, y=0)

    buscar = Listbox(personagem, width=200, height=20)
    buscar.place(x=20, y=75)

    listboxDeD.buscar_p(buscar)

    scrollbary = Scrollbar(buscar, orient=VERTICAL)
    scrollbarx = Scrollbar(buscar, orient=HORIZONTAL)
    tree = ttk.Treeview(buscar, columns=("Nome", "Raça", "Classe"), selectmode="extended", height=25, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Nome', text="Nome", anchor=W)
    tree.heading('Raça', text="Raça", anchor=W)
    tree.heading('Classe', text="Classe", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=95)
    tree.column('#2', stretch=NO, minwidth=0, width=95)
    tree.column('#3', stretch=NO, minwidth=0, width=95)
    tree.pack()

    confirmar = Button(personagem, width=20, text="Abrir Ficha")
    confirmar.place(x=135 ,y=40)
    
    voltar = Button(personagem, width=30, text="Voltar para o Menu", command=personagem.destroy)
    voltar.pack(side=BOTTOM)

    def criar_personagem():

        dados = Tk()
        dados.geometry("1250x648")
        dados.title("Criando um Personagem")

        nome = Label(dados, text="Digite o nome do seu personagem: ")
        nome.place(x=0, y=0)
        
        raca = Label(dados, text="Escolha a raça do seu personagem: ")
        raca.place(x=0, y=25)

        subraca = Label(dados, text="Escolha a sub-raça do seu personagem: ")
        subraca.place(x=0, y=50)
        
        classe = Label(dados, text="Escolha a classe do seu personagem: ")
        classe.place(x=0, y=75)

        subclasse = Label(dados, text="Escolha a sub-classe do seu personagem: ")
        subclasse.place(x=0, y=100)

        nome_personagem = Entry(dados, width=40)
        nome_personagem.place(x=197, y=0)

        racas = ['Selecione sua Raça','Anão', 'Elfo', 'Halfling', 'Humano', 'Draconato', 'Gnomo', 'Orc', 'Meio-Elfo',
                 'Meio-Orc','Tiefling', 'Goblin', 'Minotauro', 'Aarakocra', 'Tartaruga', 'Gênio', 'Golias', 'Aasimar',
                 'Shifter','Shapeshifter', 'Bugbear', 'Firbolg', 'Hobgoblin', 'Kenku', 'Kobold', 'Lagartixa', 'Tritão',
                 'Tabaxi''Yuan-Ti', 'Changeling', 'Kalashtar', 'Warforged', 'Gith', 'Centauro', 'Loxodon', 'Simic Hybrid',
                 'Vedalken', 'Locathah']

        raca_personagem = ttk.Combobox(dados, values=racas)
        raca_personagem.set('Selecione sua Raça')
        raca_personagem.place(x=196, y=25)

        subracas = ['Selecione sua Sub-Raça', '', '', '', '' , '', '', '', '', '', '', '', '', '', '',
                    '', '' ,'' , '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',]

        subraca_personagem = ttk.Combobox(dados, values=subracas)
        subraca_personagem.set('Selecione sua Sub-Raça')
        subraca_personagem.place(x=217 , y=50)

        classes = ['Selecione sua Classe','Bárbaro', 'Bardo', 'Bruxo', 'Clérigo', 'Druida',
                   'Feiticeiro','Guerreiro', 'Ladino', 'Mago', 'Monge', 'Paladino', 'Patrulheiro']
        
        classe_personagem = ttk.Combobox(dados, values=classes)
        classe_personagem.set('Selecione sua Classe')
        classe_personagem.place(x=200, y=75)

        subclasses = ['Selecione sua Sub-Classe', '', '', '', '' , '', '', '', '', '', '', '', '', '', '',
                      '', '' ,'' , '', '', '', '', '', '', '', '', '', '', '', '',
                      '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',]

        subclasse_personagem = ttk.Combobox(dados, values=subclasses)
        subclasse_personagem.set('Selecione sua Sub-Classe')
        subclasse_personagem.place(x=220 ,y=100)
        
        def pegandod():
            nome1, raca1, subraca1, classe1 = nome_personagem.get(), raca_personagem.get(), classe_personagem.get()
            BancoDeD.cadastrar_p(nome1, raca1, classe1)
            
        criar = Button(dados,width=10, text="Criar", command=pegandod)
        criar.place(x=260, y=135)
        
        voltar = Button(dados,width=10, text="Voltar", command=dados.destroy)
        voltar.pack(side=BOTTOM)

    opcao = Button(personagem, text="Se não tem um Personagem, clique aqui", command=criar_personagem)
    opcao.place(x=300 , y=40)
    


    
    
