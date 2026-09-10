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

            # False significa que a carta
            # ainda está escondida

            linha.append(False)

        matriz.append(linha)

    return matriz


def mostrar_tabuleiro(tabuleiro, reveladas):

    print("\n===================================")
    print("          JOGO DA MEMÓRIA")
    print("===================================\n")

    print("    ", end="")

    for j in range(len(tabuleiro[0])):

        print(f"{j}   ", end="")

    print()

    print("   ", end="")

    for j in range(len(tabuleiro[0])):

        print("----", end="")

    print()

    for i in range(len(tabuleiro)):

        print(f"{i} | ", end="")

        for j in range(len(tabuleiro[i])):

            if reveladas[i][j] == True:

                print(
                    f"{tabuleiro[i][j]}   ",
                    end=""
                )

            else:

                print("■   ", end="")

        print()

    print()



def validar_posicao(linha, coluna, reveladas):


    if linha < 0 or linha >= len(reveladas):

        raise IndexError(
            "Essa linha não existe no tabuleiro."
        )


    if coluna < 0 or coluna >= len(reveladas[linha]):

        raise IndexError(
            "Essa coluna não existe no tabuleiro."
        )


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


def verificar_par(
        tabuleiro,
        linha1,
        coluna1,
        linha2,
        coluna2
):

    carta1 = tabuleiro[linha1][coluna1]

    carta2 = tabuleiro[linha2][coluna2]

    if carta1 == carta2:

        return True

    else:

        return False



def mostrar_informacoes(
        pares_encontrados,
        quantidade_pares,
        tentativas
):

    print(
        f"Pares encontrados: "
        f"{pares_encontrados}/{quantidade_pares}"
    )

    print(
        f"Tentativas realizadas: "
        f"{tentativas}"
    )


def jogar():

    limpar_tela()

    linhas, colunas, quantidade_pares = escolher_nivel()


    cartas = criar_cartas(
        quantidade_pares
    )

    try:

        tabuleiro = criar_tabuleiro(
            linhas,
            colunas,
            cartas
        )

    except TypeError as erro:

        print(
            f"\nERRO DE TIPO: {erro}"
        )

        return

    except ValueError as erro:

        print(
            f"\nERRO: {erro}"
        )

        return

    reveladas = criar_matriz_reveladas(
        linhas,
        colunas
    )


    lista_pares = []


    pares_encontrados = 0

    tentativas = 0


    while pares_encontrados < quantidade_pares:

        limpar_tela()

        mostrar_tabuleiro(
            tabuleiro,
            reveladas
        )


        mostrar_informacoes(
            pares_encontrados,
            quantidade_pares,
            tentativas
        )


        print("\n------------------------------")
        print("        PRIMEIRA CARTA")
        print("------------------------------")

        linha1, coluna1 = escolher_carta(
            reveladas
        )


        reveladas[linha1][coluna1] = True


        limpar_tela()

        mostrar_tabuleiro(
            tabuleiro,
            reveladas
        )

        print("\n------------------------------")
        print("        SEGUNDA CARTA")
        print("------------------------------")

        linha2, coluna2 = escolher_carta(
            reveladas
        )

        reveladas[linha2][coluna2] = True

        tentativas = tentativas + 1

        limpar_tela()

        mostrar_tabuleiro(
            tabuleiro,
            reveladas
        )


        resultado = verificar_par(
            tabuleiro,
            linha1,
            coluna1,
            linha2,
            coluna2
        )


        if resultado == True:

            print("\nPAR ENCONTRADO!")

            simbolo_encontrado = (
                tabuleiro[linha1][coluna1]
            )

            lista_pares.append(
                simbolo_encontrado
            )

            pares_encontrados = (
                pares_encontrados + 1
            )

            print(
                f"\nSímbolo encontrado: "
                f"{simbolo_encontrado}"
            )

            print("\nPares encontrados até agora:")

            for simbolo in lista_pares:

                print(
                    simbolo,
                    end=" "
                )

            print()

            input(
                "\nPressione ENTER para continuar..."
            )
    