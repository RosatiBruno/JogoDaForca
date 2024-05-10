# Modularizando o código
def imprimirPalavraSecreta(palavra, acertos) :
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

    return adivinha

def desenharForca(erros) :
    score = 1000

    print("X==:==")
    print("X  :  ")

    if erros >= 1:
        print("X  O  ")
        score = 800

    else:
        print("X")

    linha2 = ""
    if erros == 2:
        linha2 = "  |  "
        score = 600

    elif erros == 3:
        linha2 = " /|  "
        score = 400

    elif erros >= 4:
        linha2 = " /|\ "
        score = 200

    print(f"X{linha2}")

    linha3 = ""
    if erros == 5:
        linha3 += " / "
        score = 100

    elif erros >= 6:
        linha3 += " / \ "
        score = 0

    print(f"X{linha3}")
    print(f"X\n=======")

    return score