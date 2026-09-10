import random

simbolos = [
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

def criar_cartas(quantidade_pares):

    cartas = []

    for i in range(quantidade_pares):

        simbolo = simbolos[i]


        cartas.append(simbolo)
        cartas.append(simbolo)


    random.shuffle(cartas)

    return cartas

def criar_tabuleiro(linhas, colunas, cartas):


    if type(linhas) != int or type(colunas) != int:

        raise TypeError(
            "Linhas e colunas precisam ser números inteiros."
        )


    if linhas * colunas != len(cartas):

        raise ValueError(
            "A quantidade de cartas não corresponde ao tabuleiro."
        )

    matriz = []

    indice = 0

    for i in range(linhas):

        linha = []

        for j in range(colunas):

            linha.append(cartas[indice])

            indice = indice + 1

        matriz.append(linha)

    return matriz

def criar_matriz_reveladas(linhas, colunas):

    matriz = []

    for i in range(linhas):

        linha = []

        for j in range(colunas):

            # False significa que a carta ainda está escondida
            linha.append(False)

        matriz.append(linha)

    return matriz




