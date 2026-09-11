"""
Jogo da Memória no terminal.

Este arquivo foi organizado para apresentação em sala:
- cada função tem uma responsabilidade clara;
- os comentários explicam a intenção do código;
- as validações ficam separadas do fluxo principal do jogo.
"""

import random
from typing import Dict, List, Tuple


# ============================================================================
# CONFIGURAÇÕES GERAIS
# ============================================================================

# Símbolos usados nas cartas. O jogo cria pares a partir dessa lista.
def criar_simbolos() -> List[str]:

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

    return simbolos

# Cada nível guarda: nome, quantidade de linhas, colunas e pares.
NIVEIS: Dict[int, Tuple[str, int, int, int]] = {
    1: ("Fácil", 3, 4, 6),
    2: ("Médio", 4, 4, 8),
    3: ("Difícil", 4, 6, 12),
}

CARTA_ESCONDIDA = "■"
LARGURA_CABECALHO = 35
LARGURA_BLOCO = 30


# ============================================================================
# FUNÇÕES DE APOIO VISUAL
# ============================================================================

def imprimir_cabecalho(titulo: str) -> None:
    """Mostra um título centralizado para separar as telas do jogo."""
    print(f"\n{'=' * LARGURA_CABECALHO}")
    print(f"{titulo:^{LARGURA_CABECALHO}}")
    print("=" * LARGURA_CABECALHO)


def imprimir_bloco(titulo: str) -> None:
    """Mostra um subtítulo para destacar uma etapa dentro da partida."""
    print(f"\n{'-' * LARGURA_BLOCO}")
    print(f"{titulo:^{LARGURA_BLOCO}}")
    print("-" * LARGURA_BLOCO)


def limpar_tela() -> None:
    """Simula a limpeza do terminal imprimindo várias linhas em branco."""
    print("\n" * 25)


# ============================================================================
# PREPARAÇÃO DO JOGO
# ============================================================================


def escolher_nivel() -> Tuple[int, int, int]:
    """
    Pede ao jogador o nível da partida.

    Retorna:
        linhas: quantidade de linhas do tabuleiro;
        colunas: quantidade de colunas do tabuleiro;
        quantidade_pares: total de pares que o jogador precisa encontrar.
    """
    while True:
        imprimir_cabecalho("ESCOLHA O NÍVEL")

        for codigo, (nome, linhas, colunas, pares) in NIVEIS.items():
            print(f"{codigo} - {nome:<7} - {linhas} x {colunas} - {pares} pares")

        try:
            nivel = int(input("\nDigite o nível desejado: "))

            if nivel not in NIVEIS:
                raise ValueError("Escolha somente 1, 2 ou 3.")

        except ValueError as erro:
            print(f"\nERRO: {erro}")

        else:
            _, linhas, colunas, quantidade_pares = NIVEIS[nivel]
            return linhas, colunas, quantidade_pares


def criar_cartas(quantidade_pares: int, simbolos: List[str]) -> List[str]:
    """
    Cria a lista de cartas da partida.

    Cada símbolo aparece duas vezes, formando um par. Depois disso, a lista é
    embaralhada para que o tabuleiro fique diferente a cada partida.
    """
    if quantidade_pares > len(simbolos):
        raise ValueError("Não existem símbolos suficientes para esse nível.")

    cartas: List[str] = []

    for indice in range(quantidade_pares):
        simbolo = simbolos[indice]
        cartas.extend([simbolo, simbolo])

    random.shuffle(cartas)
    return cartas


def criar_tabuleiro(
    linhas: int,
    colunas: int,
    cartas: List[str],
) -> List[List[str]]:
    """
    Transforma a lista embaralhada de cartas em uma matriz.

    Exemplo de matriz:
        [
            ["★", "♥", "★"],
            ["♣", "♥", "♣"],
        ]
    """
    if not isinstance(linhas, int) or not isinstance(colunas, int):
        raise TypeError("Linhas e colunas precisam ser números inteiros.")

    if linhas * colunas != len(cartas):
        raise ValueError("A quantidade de cartas não corresponde ao tabuleiro.")

    matriz: List[List[str]] = []

    for linha_atual in range(linhas):
        inicio = linha_atual * colunas
        fim = inicio + colunas
        matriz.append(cartas[inicio:fim])

    return matriz


def criar_matriz_reveladas(linhas: int, colunas: int) -> List[List[bool]]:
    """
    Cria uma matriz que controla quais cartas estão viradas para cima.

    False significa carta escondida.
    True significa carta revelada.
    """
    matriz: List[List[bool]] = []

    for _ in range(linhas):
        linha: List[bool] = []

        for _ in range(colunas):
            linha.append(False)

        matriz.append(linha)

    return matriz


# ============================================================================
# EXIBIÇÃO DO TABULEIRO E DAS INFORMAÇÕES
# ============================================================================

def mostrar_tabuleiro(
    tabuleiro: List[List[str]],
    reveladas: List[List[bool]],
) -> None:
    """Mostra o tabuleiro com índices de linha e coluna para orientar o jogador."""
    imprimir_cabecalho("JOGO DA MEMÓRIA")

    print("\n    ", end="")

    for coluna in range(len(tabuleiro[0])):
        print(f"{coluna:^4}", end="")

    print()
    print("   " + "----" * len(tabuleiro[0]))

    for linha in range(len(tabuleiro)):
        print(f"{linha} | ", end="")

        for coluna in range(len(tabuleiro[linha])):
            carta_visivel = reveladas[linha][coluna]
            conteudo = tabuleiro[linha][coluna] if carta_visivel else CARTA_ESCONDIDA
            print(f"{conteudo:^4}", end="")

        print()

    print()


def mostrar_informacoes(
    pares_encontrados: int,
    quantidade_pares: int,
    tentativas: int,
) -> None:
    """Mostra o progresso da partida abaixo do tabuleiro."""
    print(f"Pares encontrados: {pares_encontrados}/{quantidade_pares}")
    print(f"Tentativas realizadas: {tentativas}")


def mostrar_pares_encontrados(lista_pares: List[str]) -> None:
    """Lista os símbolos que já foram encontrados pelo jogador."""
    print("\nPares encontrados até agora:")
    print(" ".join(lista_pares))


# ============================================================================
# VALIDAÇÃO DAS JOGADAS
# ============================================================================

def validar_posicao(
    linha: int,
    coluna: int,
    reveladas: List[List[bool]],
) -> bool:
    """
    Confere se a posição escolhida existe e ainda está escondida.

    O uso de exceções deixa a função escolher_carta mais clara: ela tenta ler a
    jogada e, se algo estiver errado, apenas mostra a mensagem do erro.
    """
    if linha < 0 or linha >= len(reveladas):
        raise IndexError("Essa linha não existe no tabuleiro.")

    if coluna < 0 or coluna >= len(reveladas[linha]):
        raise IndexError("Essa coluna não existe no tabuleiro.")

    if reveladas[linha][coluna]:
        raise ValueError("Essa carta já está revelada.")

    return True


def escolher_carta(reveladas: List[List[bool]]) -> Tuple[int, int]:
    """
    Pede linha e coluna até o jogador escolher uma carta válida.

    A função só termina quando consegue retornar uma posição que pode ser usada
    no tabuleiro.
    """
    while True:
        try:
            linha = int(input("Digite a linha: "))
            coluna = int(input("Digite a coluna: "))

            validar_posicao(linha, coluna, reveladas)

        except ValueError as erro:
            print(f"\nERRO DE ENTRADA: {erro}")

        except IndexError as erro:
            print(f"\nERRO DE POSIÇÃO: {erro}")

        else:
            return linha, coluna

        finally:
            print("-" * LARGURA_BLOCO)


def verificar_par(
    tabuleiro: List[List[str]],
    linha1: int,
    coluna1: int,
    linha2: int,
    coluna2: int,
) -> bool:
    """Compara duas cartas e informa se elas formam um par."""
    carta1 = tabuleiro[linha1][coluna1]
    carta2 = tabuleiro[linha2][coluna2]

    return carta1 == carta2


# ============================================================================
# FLUXO PRINCIPAL DA PARTIDA
# ============================================================================

def jogar() -> None:
    """Controla uma partida completa do jogo da memória."""
    limpar_tela()

    # Etapa 1: o jogador escolhe o tamanho do desafio.
    linhas, colunas, quantidade_pares = escolher_nivel()

    # Etapa 2: o programa monta o baralho, o tabuleiro e o controle visual.
    simbolos = criar_simbolos()
    cartas = criar_cartas(quantidade_pares, simbolos)

    try:
        tabuleiro = criar_tabuleiro(linhas, colunas, cartas)

    except TypeError as erro:
        print(f"\nERRO DE TIPO: {erro}")
        return

    except ValueError as erro:
        print(f"\nERRO: {erro}")
        return

    reveladas = criar_matriz_reveladas(linhas, colunas)
    lista_pares: List[str] = []
    pares_encontrados = 0
    tentativas = 0

    # Etapa 3: o laço continua até todos os pares serem encontrados.
    while pares_encontrados < quantidade_pares:
        limpar_tela()

        mostrar_tabuleiro(tabuleiro, reveladas)
        mostrar_informacoes(pares_encontrados, quantidade_pares, tentativas)

        imprimir_bloco("PRIMEIRA CARTA")
        linha1, coluna1 = escolher_carta(reveladas)
        reveladas[linha1][coluna1] = True

        limpar_tela()
        mostrar_tabuleiro(tabuleiro, reveladas)

        imprimir_bloco("SEGUNDA CARTA")
        linha2, coluna2 = escolher_carta(reveladas)
        reveladas[linha2][coluna2] = True

        tentativas += 1

        limpar_tela()
        mostrar_tabuleiro(tabuleiro, reveladas)

        resultado = verificar_par(tabuleiro, linha1, coluna1, linha2, coluna2)

        if resultado:
            print("\nPAR ENCONTRADO!")

            simbolo_encontrado = tabuleiro[linha1][coluna1]
            lista_pares.append(simbolo_encontrado)
            pares_encontrados += 1

            print(f"\nSímbolo encontrado: {simbolo_encontrado}")
            mostrar_pares_encontrados(lista_pares)

            input("\nPressione ENTER para continuar...")

        else:
            print("\nAs cartas são diferentes.")
            input("\nPressione ENTER para escondê-las novamente...")

            # Quando não há par, as duas cartas voltam a ficar escondidas.
            reveladas[linha1][coluna1] = False
            reveladas[linha2][coluna2] = False

    limpar_tela()
    mostrar_tabuleiro(tabuleiro, reveladas)

    imprimir_cabecalho("VOCÊ GANHOU!")
    print(f"\nVocê encontrou todos os {quantidade_pares} pares!")
    print(f"Total de tentativas: {tentativas}")

    print("\nSímbolos encontrados:")
    print(" ".join(lista_pares))
    print()


# ============================================================================
# MENU E TELA DE AJUDA
# ============================================================================

def mostrar_como_jogar() -> None:
    """Explica as regras antes de iniciar uma partida."""
    limpar_tela()

    simbolos = criar_simbolos()

    imprimir_cabecalho("COMO JOGAR")

    print("\nObjetivo:")
    print("Encontrar todos os pares de símbolos do tabuleiro.")

    print("\nComo funciona:")
    print("1. Escolha a linha e a coluna da primeira carta.")
    print("2. Escolha a linha e a coluna da segunda carta.")
    print("3. Se forem iguais, elas continuam abertas.")
    print("4. Se forem diferentes, elas voltam a ficar escondidas.")

    print("\nSímbolos utilizados:")
    print("  ".join(simbolos))

    print("\nNíveis disponíveis:")

    for codigo, (nome, linhas, colunas, pares) in NIVEIS.items():
        print(
            f"{codigo} - {nome}: "
            f"{linhas} linhas x {colunas} colunas | {pares} pares"
        )

    input("\nPressione ENTER para voltar ao menu...")
    limpar_tela()


def iniciar_programa() -> None:
    """Exibe o menu principal e direciona o usuário para cada parte do jogo."""
    while True:
        imprimir_cabecalho("JOGO DA MEMÓRIA")

        print("\n1 - Jogar")
        print("2 - Como jogar")
        print("3 - Encerrar")

        try:
            opcao = int(input("\nEscolha uma opção: "))

            if opcao < 1 or opcao > 3:
                raise ValueError("Escolha somente 1, 2 ou 3.")

        except ValueError as erro:
            print(f"\nERRO: {erro}")

        else:
            if opcao == 1:
                jogar()

            elif opcao == 2:
                mostrar_como_jogar()

            elif opcao == 3:
                print("\nPrograma encerrado.")
                break

        finally:
            print("\n" + "-" * LARGURA_CABECALHO)


if __name__ == "__main__":
    iniciar_programa()
