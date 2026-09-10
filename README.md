# Jogo da Memória em Python

Projeto desenvolvido para o **Checkpoint 4 de Computational Thinking using Python**.

O objetivo foi criar um jogo de tabuleiro utilizando **estruturas bidimensionais (matrizes)**, funções, listas, estruturas condicionais, estruturas de repetição e tratamento de erros.

---

## Repositório

**GitHub:** `COLOCAR_LINK_DO_REPOSITORIO_AQUI`

---

## Sobre o jogo

O projeto é um **Jogo da Memória executado no terminal**.

O jogador escolhe duas posições do tabuleiro informando a **linha** e a **coluna** de cada carta. As cartas ficam escondidas e são representadas pelo símbolo `■`.

Quando uma posição é escolhida, o símbolo daquela carta é revelado.

- Se as duas cartas forem iguais, o par permanece aberto.
- Se forem diferentes, elas são escondidas novamente.
- O jogo continua até que todos os pares sejam encontrados.

O programa também registra a quantidade de tentativas realizadas durante a partida.

---

## Níveis de dificuldade

Antes de iniciar a partida, o jogador escolhe o nível desejado.

| Nível | Tabuleiro | Cartas | Pares |
|---|---:|---:|---:|
| Fácil | 3 x 4 | 12 | 6 |
| Médio | 4 x 4 | 16 | 8 |
| Difícil | 4 x 6 | 24 | 12 |

A dificuldade aumenta principalmente pela quantidade de posições e pares que precisam ser memorizados.

### Por que não existe limite de tentativas?

Optamos por não limitar a quantidade de tentativas porque a proposta segue a lógica tradicional de um jogo da memória.

O jogador pode continuar tentando até encontrar todos os pares. A quantidade de tentativas funciona como um **indicador de desempenho**: quanto menos tentativas forem necessárias, melhor foi o desempenho na partida.

Além disso, um limite muito baixo poderia encerrar a partida antes que o jogador conseguisse completar o tabuleiro, principalmente no nível difícil.

---

## Símbolos utilizados

As cartas utilizam símbolos para facilitar a visualização diretamente no console:

`★  ♥  ◆  ♣  ♠  ☀  ☂  ♫  ☾  ✿  ✦  ☯`

Cada símbolo aparece duas vezes no tabuleiro, formando um par.

A biblioteca `random` é utilizada para embaralhar as cartas antes da criação da matriz.

---

## Como o jogo funciona

O fluxo principal do programa é:

1. O programa exibe o menu principal.
2. O jogador escolhe entre jogar, visualizar as instruções ou encerrar.
3. Ao iniciar uma partida, o jogador escolhe o nível de dificuldade.
4. O programa cria os pares de símbolos.
5. As cartas são embaralhadas.
6. A lista de cartas é transformada em uma matriz.
7. É criada uma segunda matriz para controlar quais cartas estão reveladas.
8. O jogador escolhe a primeira carta usando linha e coluna.
9. O jogador escolhe a segunda carta.
10. O programa compara os dois símbolos.
11. Se forem iguais, o par permanece revelado.
12. Se forem diferentes, as cartas são escondidas novamente.
13. O processo se repete até todos os pares serem encontrados.
14. Ao final, o programa informa a vitória e o total de tentativas.

---

## Estruturas utilizadas

### Matriz do tabuleiro

O tabuleiro é representado por uma **lista de listas**.

Exemplo:

```python
[
    ["★", "♥", "◆", "★"],
    ["♣", "♥", "♠", "☀"],
    ["☀", "◆", "♠", "♣"]
]
```

Cada posição pode ser acessada utilizando dois índices:

```python
tabuleiro[linha][coluna]
```

### Matriz de cartas reveladas

Existe uma segunda matriz que possui o mesmo tamanho do tabuleiro.

Ela utiliza valores booleanos:

- `False` = carta escondida
- `True` = carta revelada

Exemplo:

```python
[
    [False, False, True, False],
    [False, True, False, False],
    [False, False, False, False]
]
```

Essa matriz permite controlar o que deve aparecer para o jogador sem modificar o conteúdo original do tabuleiro.

---

# Principais funções

## `criar_simbolos()`

Cria e retorna a lista com os símbolos utilizados nas cartas.

A criação dos símbolos dentro de uma função evita depender de uma lista global para o funcionamento do jogo.

---

## `escolher_nivel()`

Exibe os três níveis disponíveis e recebe a escolha do jogador.

A função define e retorna:

- quantidade de linhas;
- quantidade de colunas;
- quantidade de pares.

Também realiza tratamento de erro caso seja digitada uma opção inválida.

---

## `criar_cartas()`

Recebe a quantidade de pares e a lista de símbolos.

Cada símbolo necessário é inserido duas vezes na lista para formar os pares.

Depois disso, `random.shuffle()` é utilizado para embaralhar as cartas.

---

## `criar_tabuleiro()`

Transforma a lista de cartas em uma estrutura bidimensional.

Também verifica se o número de linhas e colunas é válido e se a quantidade de cartas corresponde ao tamanho do tabuleiro.

---

## `criar_matriz_reveladas()`

Cria uma matriz de valores `False` com o mesmo tamanho do tabuleiro.

Essa matriz controla quais cartas estão escondidas ou reveladas durante a partida.

---

## `mostrar_tabuleiro()`

Percorre o tabuleiro utilizando dois laços de repetição.

Se a posição estiver marcada como `True` na matriz de controle, o símbolo é exibido. Caso contrário, aparece `■`.

A função também mostra os números das linhas e colunas para orientar o jogador.

---

## `validar_posicao()`

Confere se a linha e a coluna escolhidas são válidas.

Ela impede:

- linhas inexistentes;
- colunas inexistentes;
- escolha de uma carta que já esteja revelada.

Para isso, são utilizadas exceções como `IndexError` e `ValueError`.

---

## `escolher_carta()`

Recebe a matriz de controle e solicita linha e coluna ao jogador.

Utiliza:

```python
try
except
else
finally
```

Caso a entrada seja inválida, o jogador recebe uma mensagem de erro e pode tentar novamente.

---

## `verificar_par()`

Recebe as posições das duas cartas escolhidas e compara seus valores.

Retorna:

- `True` quando as cartas formam um par;
- `False` quando são diferentes.

---

## `mostrar_informacoes()`

Mostra o progresso da partida, incluindo:

- pares encontrados;
- quantidade total de pares;
- número de tentativas.

---

## `mostrar_pares_encontrados()`

Exibe os símbolos dos pares que já foram encontrados durante a partida.

---

## `jogar()`

É a principal função do jogo.

Ela conecta as demais funções e controla toda a partida.

Dentro dela são realizadas etapas como:

- escolha do nível;
- criação das cartas;
- criação do tabuleiro;
- criação da matriz de controle;
- escolha das duas cartas;
- comparação dos símbolos;
- atualização das cartas reveladas;
- contagem das tentativas;
- contagem dos pares encontrados;
- condição de vitória.

---

## `mostrar_como_jogar()`

Exibe as regras, os níveis disponíveis e os símbolos utilizados no jogo.

---

## `iniciar_programa()`

Controla o menu principal.

O jogador pode escolher:

1. Jogar
2. Como jogar
3. Encerrar

Também possui tratamento de erro para impedir opções inválidas.

---

# Tratamento de erros

O projeto utiliza tratamento de exceções para evitar que entradas incorretas encerrem o programa.

### `ValueError`

É utilizado, por exemplo, quando:

- o jogador digita uma letra onde deveria informar um número;
- escolhe uma opção inexistente;
- tenta escolher uma carta que já está revelada.

### `IndexError`

É utilizado quando a linha ou coluna escolhida não existe no tabuleiro.

### `TypeError`

É utilizado na criação do tabuleiro para validar o tipo dos valores recebidos.

### `raise`

O `raise` é utilizado para gerar uma exceção propositalmente quando uma regra do programa não é respeitada.

---

# Conceitos de Python aplicados

Durante o desenvolvimento foram utilizados:

- variáveis;
- listas;
- listas de listas;
- matrizes;
- strings;
- dicionários/estruturas de configuração;
- funções;
- parâmetros;
- retorno de funções;
- `if`, `elif` e `else`;
- `for`;
- `while`;
- `try`, `except`, `else` e `finally`;
- `raise`;
- `ValueError`;
- `IndexError`;
- `TypeError`;
- valores booleanos;
- manipulação de índices;
- biblioteca `random`.

---

# Divisão das responsabilidades

## Yasmin — Pessoa 1

Yasmin participou principalmente da **estrutura inicial e preparação do jogo**.

Suas atividades envolveram apoio na implementação de partes como:

- definição inicial dos símbolos;
- níveis de dificuldade;
- preparação das cartas;
- estrutura inicial do tabuleiro;
- organização das primeiras funções necessárias para iniciar uma partida.

Sua participação ajudou a construir a base utilizada pelas demais etapas do projeto.

---

## Lívia — Pessoa 2

Lívia participou principalmente da **interação do jogador com o tabuleiro e controle das posições**.

Suas atividades envolveram apoio na implementação de partes como:

- matriz de cartas reveladas;
- exibição do tabuleiro;
- entrada de linha e coluna;
- validação das posições escolhidas;
- tratamento de entradas inválidas;
- lógica inicial de seleção da primeira e segunda carta.

Essa parte foi importante para permitir que o usuário realmente interagisse com a matriz criada pelo programa.

---

## Manuela — Pessoa 3

Manuela ficou responsável principalmente pela **integração, finalização e organização geral do projeto**.

Além de participar da implementação, ficou responsável por conectar as partes desenvolvidas anteriormente e garantir que o jogo funcionasse como uma única aplicação.

Entre suas principais responsabilidades estão:

- integração das funções desenvolvidas pelo grupo;
- implementação e revisão da lógica de comparação dos pares;
- comportamento das cartas após acerto ou erro;
- controle de pares encontrados;
- contagem das tentativas;
- condição de vitória;
- fluxo principal da função `jogar()`;
- organização do menu principal;
- tela de instruções;
- revisão das validações;
- revisão e limpeza do código final;
- padronização da indentação e dos comentários;
- organização da entrega;
- documentação do projeto.

A etapa final também envolveu revisar partes que haviam sido implementadas separadamente para garantir que todas funcionassem corretamente quando integradas.

---

# Organização do desenvolvimento

O projeto foi desenvolvido de forma incremental por meio de commits.

Cada integrante ficou responsável por partes específicas, e as funcionalidades foram sendo adicionadas gradualmente.

Após a implementação das partes individuais, foi realizada uma etapa de integração e revisão para corrigir incompatibilidades, remover redundâncias e garantir que o código final funcionasse de forma consistente.

---

# Transparência sobre o uso de Inteligência Artificial

Ferramentas de Inteligência Artificial foram utilizadas como **apoio durante a etapa de revisão e documentação do trabalho**.

A IA auxiliou principalmente em:

- organização desta documentação;
- melhoria da clareza dos textos explicativos;
- revisão da apresentação visual do código;
- padronização de indentação;
- melhoria e organização de comentários;
- identificação de possíveis problemas de organização;
- revisão final do código e da entrega.

Um exemplo ocorreu durante a revisão da estrutura dos símbolos. Em uma versão anterior, a lista utilizada pelo jogo estava sendo tratada como uma variável global. Durante a revisão, foi identificado que essa estrutura poderia entrar em conflito com os critérios propostos para o trabalho. A partir disso, o grupo reorganizou essa parte por meio de uma função responsável por fornecer os símbolos utilizados pelo jogo.

A Inteligência Artificial também foi utilizada depois da implementação dos commits para auxiliar na **limpeza e legibilidade do código**, deixando funções, comentários e espaçamentos mais claros para a apresentação.

No entanto, a **ideia do jogo, as regras, a escolha dos níveis, a lógica principal, a implementação das funcionalidades e as decisões do projeto foram desenvolvidas pelo grupo**. A ferramenta foi utilizada como apoio para revisão, correção, clareza e apresentação da entrega final.

---

# Como executar

É necessário possuir o Python instalado.

No terminal, execute:

```bash
python jogo_memoria.py
```

Depois escolha uma das opções exibidas no menu.

---

# Conclusão

O projeto permitiu aplicar os principais conceitos trabalhados em Python em uma situação prática.

A utilização de matrizes foi essencial para representar o tabuleiro, enquanto a segunda matriz permitiu controlar o estado das cartas durante a partida.

As funções ajudaram a separar as responsabilidades do programa, e o tratamento de erros tornou a interação mais segura e compreensível para o usuário.

Os diferentes níveis permitem variar o tamanho do desafio sem alterar a lógica principal do jogo, demonstrando como uma mesma estrutura pode ser reutilizada em diferentes configurações.
