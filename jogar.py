from jogo_memoria import (
    criar_matriz_reveladas,
    criar_tabuleiro,
    mostrar_tabuleiro,
    escolher_carta
)

def jogar(linhas, colunas, cartas, quantidade_pares):

    tabuleiro = criar_tabuleiro(
        linhas,
        colunas,
        cartas
    )

    reveladas = criar_matriz_reveladas(
        linhas,
        colunas
    )

    pares_encontrados = 0
    tentativas = 0

    while pares_encontrados < quantidade_pares:

        mostrar_tabuleiro(
            tabuleiro,
            reveladas
)

        print(f"\nTentativas: {tentativas}")
        print(f"Pares encontrados: {pares_encontrados}")

        print("\nEscolha a primeira carta:")

        linha1, coluna1 = escolher_carta(
            reveladas
        )

        reveladas[linha1][coluna1] = True

        mostrar_tabuleiro(
            tabuleiro,
            reveladas
)

        print("\nEscolha a segunda carta:")

        linha2, coluna2 = escolher_carta(
            reveladas
        )

        reveladas[linha2][coluna2] = True

        tentativas += 1

        mostrar_tabuleiro(
            tabuleiro,
            reveladas
)