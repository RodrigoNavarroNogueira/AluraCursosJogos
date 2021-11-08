from random import randint


def jogar():
    computador = randint(1, 10)
    tentativas = 0
    dificuldade = 0
    mensagem_de_abertura()

    print("Níveis de dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")

    while dificuldade not in [1, 2, 3]:
        dificuldade = int(input('Qual dificuldade você deseja?'))
        if dificuldade == 1:
            tentativas = 5

        elif dificuldade == 2:
            tentativas = 4

        elif dificuldade == 3:
            tentativas = 3

        else:
            print('Selecione uma opção válida!')

    for c in range(1, tentativas +1):
        print(f'Tentativa {c} de {tentativas}')

        jogador = int(input('Qual seu chute?'))
        if jogador < 0 or jogador > 10:
            print('Você deve pensar em um número de 1 á 10!')

        if jogador == computador:
            imprime_mensagem_vencedor()
            break

        else:
            if jogador > computador:
                if c < tentativas:
                    print('Pensei em um número menor')

            elif jogador < computador:
                if c < tentativas:
                    print('Pensei em um número maior')

        if c == tentativas:
            imprime_mensagem_perdedor(computador)


def mensagem_de_abertura():
    print("*********************************")
    print("Bem vindo ao jogo da Adivinhação!")
    print("*********************************")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(computador):
    print("Poxa, você perdeu!")
    print(f"Pensei no número {computador}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if __name__ == "__main__":
    jogar()
