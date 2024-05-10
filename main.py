import bd
import jogo as j
import time as t

def mostrarMenu() :
    print("=" * 30)
    print("JOGO DA FORCA".center(30))
    print("=" * 30)
    print("\n1 - JOGAR")
    print("2 - SCORE")
    print("3 - REMOVER SCORES")
    print("4 - SAIR")

conn = None

while True :
    conn = bd.conectar(conn)
    bd.criarTabela(conn)

    mostrarMenu()

    opcao = int(input("Digite a opção desejada (1/2/3/4): "))

    if opcao == 1 :
        print("Iniciando o jogo!")
        t.sleep(1)
        j.jogar(conn)

    elif opcao == 2 :
        print("SCORE: ")
        dados = bd.listarDado(conn)

        if not dados :
            print("Não existem scores salvos!")

        else :
            i = 1
            for jogador in dados :
                print(f"{i} -> {jogador[1]}, Pontuação: {jogador[2]}")
                i += 1
        input("\nPressione qualquer tecla para continuar...")

    elif opcao == 3:
        print("Removendo Scores salvos...")
        t.sleep(2)
        bd.removerDadosDoBanco(conn)
        mostrarMenu()

    elif opcao == 4 :
        print("Saindo do Jogo!")
        t.sleep(1)
        break

    else :
        print("Opção inválida! Tente novamente!")
        t.sleep(1)
        mostrarMenu()

bd.desconectar(conn)