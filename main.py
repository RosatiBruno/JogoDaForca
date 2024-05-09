#Pede a digitação da palavra a ser acertada, converte ela para toda minúscula e remove espaços em branco no ínicio e fim
palavra = input("Digite uma palavra secreta: ").lower().strip()

#Pula 50 linhas para "limpar" o terminal e a outra pessoa não ver a palavra secreta
for x in range(50) :
    print()

digitadas = []  #Guarda as letras que já foram digitadas
acertos = []    #Guarda as letras qua já forem acertadas
erros = 0       #Armazena a qtd de erros até o usuário perder

while True :
    adivinha = ""

    for letra in palavra :

        if letra in acertos :
            adivinha += letra   #A palavra recebe a letra que foi acertada

        else :
            adivinha += "\u2588"    #Código unicode do quadradinho p/ letras não acertadas (Mudar aqui caso queira mudar o quadradinho)

    print(f"ADIVINHE ({len(palavra)} letras): ")

    for letra in adivinha :
        print(f"{letra} ", end="")
    print()

    # Condição de vitória
    if adivinha == palavra :
        print("Parabéns! Você acertou a palavra!")
        break

    # Chute de letra
    tentativa = input("\nDigite uma letra: ").lower().strip()

    if tentativa in digitadas :
        print("Você já chutou essa letra.")
        continue                    #Retorna para o início do laço inicial While True caso a pessoa chute uma letra já digitada

    else :
        digitadas += tentativa

        if tentativa in palavra :   #Se a letra chutada estiver na palavra secreta
            acertos += tentativa

        else :                      #Se a letra chutada não estiver na palavra secreta, adicioma 1 erro
            erros += 1
            print("Você errou!")

    #Desenhando a forca
    print("X==:==")
    print("X  :  ")

    if erros >= 1 :
        print("X  O  ")

    else :
        print("X")

    linha2 = ""
    if erros == 2 :
        linha2 = "  |  "
    elif erros == 3 :
        linha2 = " /|  "
    elif erros >= 4 :
        linha2 = " /|\ "
    print(f"X{linha2}")

    linha3 = ""
    if erros == 5 :
        linha3 += " / "
    elif erros >= 6 :
        linha3 += " / \ "

    print(f"X{linha3}")
    print(f"X\n=======")

    # Condição de Perder o Jogo
    if erros == 6 :
        print("Enforcado!")
        print(f"A palavra era {palavra}")
        break