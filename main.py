import jogo as j
import time as t

def mostrarMenu() :
    print("=" * 30)
    print("JOGO DA FORCA".center(30))
    print("=" * 30)
    print("\n1 - JOGAR")
    print("2 - SCORE")
    print("3 - SAIR")

while True :
    mostrarMenu()

    opcao = int(input("Digite a opção desejada (1/2/3): "))

    if opcao == 1 :
        print("Iniciando o jogo!")
        t.sleep(1)
        j.jogar()


    elif opcao == 2 :
        print("Scores")

    elif opcao == 3 :
        print("Saindo do Jogo!")
        t.sleep(1)
        break

    else :
        print("Opção inválida! Tente novamente!")
        t.sleep(1)
        mostrarMenu()
