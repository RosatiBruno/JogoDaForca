#importa os outros arquivos (desenhos.py e random)
import desenhos as d
from random import choice

def jogar() :
    for i in range (50) :
        print(" ")

    listaPalavras = list()
    arquivo = open("palavras.txt", "r")     #Pega palavra por palavra do TXT e vai atribuindo ao arquivo

    for linha in arquivo :
        palavra = linha.strip()
        listaPalavras.append(palavra)       #Pega todas as palavras do arquivo e coloca na lista de palavras

    palavraSorteada = choice(listaPalavras)     #Escolhe aleatoriamente uma palavra que está na lista de palavras


    digitadas = []  #Guarda as letras que já foram digitadas
    acertos = []    #Guarda as letras qua já forem acertadas
    erros = 0       #Armazena a qtd de erros até o usuário perder

    while True :
        adivinha = d.imprimirPalavraSecreta(palavraSorteada, acertos)

        # Condição de vitória
        if adivinha == palavraSorteada :
            print("Parabéns! Você acertou a palavra!")
            break

        # Chute de letra
        tentativa = input("\nDigite uma letra: ").lower().strip()

        if tentativa in digitadas :
            print("Você já chutou essa letra.")
            continue                    #Retorna para o início do laço inicial While True caso a pessoa chute uma letra já digitada

        else :
            digitadas += tentativa

            if tentativa in palavraSorteada :   #Se a letra chutada estiver na palavra secreta
                acertos += tentativa

            else :                      #Se a letra chutada não estiver na palavra secreta, adiciona 1 erro
                erros += 1
                print("Você errou!")

        d.desenharForca(erros)

        # Condição de Perder o Jogo
        if erros == 6 :
            print("Enforcado!")
            print(f"A palavra era {palavraSorteada}")
            break