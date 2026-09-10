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

def mostrar_tabuleiro(tabuleiro, reveladas):

    print("\n===================================")
    print(" JOGO DA MEMÓRIA")
    print("===================================\n")

    # Mostra o número das colunas
    print(" ", end="")

    for j in range(len(tabuleiro[0])):
        print(f"{j} ", end="")

    print()

    print(" ", end="")

    for j in range(len(tabuleiro[0])):
        print("----", end="")

    print()

    # Percorre a matriz
    for i in range(len(tabuleiro)):

        # Mostra o número da linha
        print(f"{i} | ", end="")

        for j in range(len(tabuleiro[i])):

            # Se a carta estiver revelada, mostra o símbolo
            if reveladas[i][j] == True:
                print(
                    f"{tabuleiro[i][j]} ",
                    end=""
                )

            # Se estiver escondida, mostra um quadrado
            else:
                print("■ ", end="")

        print()

def validar_posicao(linha, coluna, reveladas):

    # Verifica se a linha existe
    if linha < 0 or linha >= len(reveladas):
        raise IndexError(
            "Essa linha não existe no tabuleiro."
        )

    # Verifica se a coluna existe
    if coluna < 0 or coluna >= len(reveladas[linha]):
        raise IndexError(
            "Essa coluna não existe no tabuleiro."
        )

    # Não permite escolher uma carta
    # que já esteja aberta
    if reveladas[linha][coluna] == True:
        raise ValueError(
            "Essa carta já está revelada."
        )

    return True

def escolher_carta(reveladas):

    while True:

        try:

            linha = int(
                input("Digite a linha: ")
            )

            coluna = int(
                input("Digite a coluna: ")
            )

            validar_posicao(
                linha,
                coluna,
                reveladas
            )

        except ValueError as erro:

            print(
                f"\nERRO DE ENTRADA: {erro}"
            )

        except IndexError as erro:

            print(
                f"\nERRO DE POSIÇÃO: {erro}"
            )

        else:

            return linha, coluna

        finally:

            print("-" * 30)
  



