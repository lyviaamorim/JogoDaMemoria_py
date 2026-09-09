import random

[
    "★",
    "♥",
    "◆",
    "♣",
    "♠",
    "☀",
    "☂",
    "♫",
    "☾",
    "✿",
    "✦",
    "☯"
]

def limpar_tela():
    print("\n" * 25)

def escolher_nivel():

    while True:

        print("\n===================================")
        print("          ESCOLHA O NÍVEL")
        print("===================================")

        print("1 - Fácil   - 3 x 4 - 6 pares")
        print("2 - Médio   - 4 x 4 - 8 pares")
        print("3 - Difícil - 4 x 6 - 12 pares")

        try:

            nivel = int(
                input("\nDigite o nível desejado: ")
            )

            if nivel < 1 or nivel > 3:

                raise ValueError(
                    "Escolha somente 1, 2 ou 3."
                )

        except ValueError as erro:

            print(f"\nERRO: {erro}")

        else:

            if nivel == 1:

                linhas = 3
                colunas = 4
                quantidade_pares = 6

            elif nivel == 2:

                linhas = 4
                colunas = 4
                quantidade_pares = 8

            else:

                linhas = 4
                colunas = 6
                quantidade_pares = 12

            return linhas, colunas, quantidade_pares
