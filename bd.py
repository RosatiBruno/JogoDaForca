import sqlite3
import os

def conectar(conn) :

    conn = sqlite3.connect("score.db")
    return conn

def desconectar(conn) :
    conn.close()

def criarTabela(conn) : #Cria a tabela dentro do banco
    cursor = conn.cursor()
    #Consulta SQL
    cursor.execute("""
        
    create table if not exists scoreJogo (
        id integer not null primary key autoincrement,
        nome text not null,
        valorScore integer not null
    ) 
        
    """)
    conn.commit()

def inserirDado(conn, nome, valor) :
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scoreJogo (nome, valorScore) VALUES (?, ?)", (nome, valor))

    #cursor.execute("""
    
     #   insert into scoreJogo (nome, valorScore) values (?, ?)
    
    #""", (nome, valor))
    conn.commit()
    #desconectar(conn)


def listarDado(conn):

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scoreJogo ORDER BY valorScore DESC")
    dados = cursor.fetchall()
    return dados

#Usado para remover todos os dados presentes no banco
def removerDadosDoBanco(conn) :
    cursor = conn.cursor()
    cursor.execute("DELETE FROM scoreJogo")
    conn.commit()