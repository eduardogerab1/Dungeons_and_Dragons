import sqlite3
from tkinter import messagebox

def banco():
    conn = sqlite3.connect("DeD.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
    Nome TEXT NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS personagens(
    Nome TEXT NOT NULL,
    Raca TEXT NOT NULL,
    Classe TEXT NOT NULL
    );
    """)

#   USUARIOS

def cadastrar_u(nome):
    conn = sqlite3.connect("DeD.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO usuarios (Nome)
    VALUES(?)
    """, (nome,))
    conn.commit()
    messagebox.showinfo("Cadastro", "Usuario cadastrado com sucesso")
    conn.close()

def consultar_u(nome,pesquisa):
    pesquisa.delete(0)
    conn = sqlite3.connect("DeD.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM usuarios WHERE Nome = ?""",(nome,))
    var = cursor.fetchall()
    pesquisa.insert(0,var)

def atualizar_u(novo_nome, nome):

    conn = sqlite3.connect("DeD.db")
    cursor = conn.cursor()
    cursor.execute("""UPDATE usuarios SET Nome = ? WHERE Nome = ?""", (novo_nome, nome,))
    messagebox.showinfo('Atualizar', 'Dados do usuario atualizados com sucesso')
    conn.commit()
    conn.close()

def apagar_u(nome):

    conn = sqlite3.connect("DeD.db")
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM usuarios WHERE Nome = ?""", (nome,))
    messagebox.showinfo('Deletar', 'Usuario deletado com sucesso')
    conn.commit()
    conn.close()

#  PERSONAGENS

def cadastrar_p(nome, raca, classe):
    conn = sqlite3.connect("DeD.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO personagens (Nome, Raca, Classe)
    VALUES(?,?,?)
    """, (nome, raca, classe,))
    conn.commit()
    messagebox.showinfo("Cadastro", "Personagem Cadastrado com sucesso")
    conn.close()

def consultar_p(nome,pesquisa):
    pesquisa.delete(0)
    conn = sqlite3.connect("DeD.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM personagens WHERE Nome = ?""",(nome,))
    var = cursor.fetchall()
    pesquisa.insert(0,var)

def atualizar_p(novo_nome, nova_raca, nova_classe,nome):

    conn = sqlite3.connect("DeD.db")
    cursor = conn.cursor()
    cursor.execute("""UPDATE personagens
     SET Nome = ?,
      Raca = ?, 
      Classe = ?
      WHERE Nome = ?""", (novo_nome, nova_raca, nova_classe,nome,))
    messagebox.showinfo('Atualizar', 'Personagem atualizado com sucesso')
    conn.commit()
    conn.close()

def apagar_p(nome):

    conn = sqlite3.connect("DeD.db")
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM personagens WHERE Nome = ?""", (nome,))
    messagebox.showinfo('Deletar', 'Personagem deletado com sucesso')
    conn.commit()
    conn.close()

    
