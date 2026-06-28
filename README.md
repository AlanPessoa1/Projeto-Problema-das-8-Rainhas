# Problema das 8 Rainhas

Este projeto apresenta uma solução para o **Problema das 8 Rainhas** utilizando a técnica de **backtracking**.

O objetivo do problema é posicionar 8 rainhas em um tabuleiro de xadrez 8x8 de forma que nenhuma rainha ataque outra. Assim, duas rainhas não podem estar na mesma linha, na mesma coluna ou na mesma diagonal.

## Técnica utilizada

A técnica utilizada foi o **backtracking**, uma estratégia algorítmica baseada na construção incremental de soluções.

O algoritmo posiciona uma rainha por linha. Para cada linha, ele testa as colunas disponíveis e verifica se a posição escolhida é válida. Caso a posição seja válida, o algoritmo posiciona temporariamente a rainha e avança para a próxima linha. Caso aquele caminho não leve a uma solução completa, a escolha é desfeita e uma nova possibilidade é testada.

Esse processo continua até que todas as soluções possíveis sejam encontradas.

## Representação da solução

Cada solução é representada por uma lista, em que:

* o índice representa a linha do tabuleiro;
* o valor armazenado representa a coluna onde a rainha foi posicionada.

Por exemplo, a lista:

```python
[0, 4, 7, 5, 2, 6, 1, 3]
```

indica que:

* na linha 0, a rainha está na coluna 0;
* na linha 1, a rainha está na coluna 4;
* na linha 2, a rainha está na coluna 7;
* e assim sucessivamente.

Essa representação evita a necessidade de armazenar uma matriz 8x8 completa, pois cada linha possui exatamente uma rainha.

## Verificação de conflitos

Para verificar se uma posição é válida, o algoritmo utiliza três conjuntos auxiliares:

```python
colunas_ocupadas
diagonais_principais_ocupadas
diagonais_secundarias_ocupadas
```

Uma posição é considerada inválida se já existir uma rainha:

* na mesma coluna;
* na mesma diagonal principal;
* na mesma diagonal secundária.

As diagonais são identificadas pelas seguintes relações:

```python
diagonal_principal = linha - coluna
diagonal_secundaria = linha + coluna
```

Dessa forma, a verificação de conflitos é feita de maneira simples e eficiente.

## Como executar

Para executar o projeto, utilize:

```bash
python main.py
```

O programa não depende de bibliotecas externas. Ele utiliza apenas recursos nativos da linguagem Python.

## O que o programa faz

Ao ser executado, o programa:

1. resolve o Problema das 8 Rainhas;
2. exibe no terminal a primeira solução encontrada;
3. salva todas as soluções no arquivo `outputs/solucoes.txt`;
4. salva estatísticas da execução no arquivo `outputs/estatisticas.txt`;
5. gera imagens em SVG de algumas soluções na pasta `outputs/imagens`.

## Resultado

Para o caso clássico com 8 rainhas, o algoritmo encontra:

```txt
Total de soluções encontradas: 92
```

## Estatísticas da execução

A execução do algoritmo para `n = 8` gerou os seguintes dados:

```txt
Total de soluções encontradas: 92
Chamadas recursivas: 2057
Tentativas de posicionamento: 15720
Posições válidas testadas: 2056
Retrocessos realizados: 2056
```

Essas estatísticas ajudam a observar o comportamento do backtracking durante a busca. O algoritmo avaliou 15720 tentativas de posicionamento, mas apenas 2056 foram consideradas válidas em relação às restrições de coluna e diagonais.

## Arquivos gerados

Após a execução, são gerados os seguintes arquivos:

```txt
outputs/solucoes.txt
outputs/estatisticas.txt
outputs/imagens/solucao_1.svg
outputs/imagens/solucao_2.svg
outputs/imagens/solucao_3.svg
outputs/imagens/solucao_4.svg
outputs/imagens/solucao_5.svg
```

O arquivo `solucoes.txt` contém todas as 92 soluções encontradas. O arquivo `estatisticas.txt` contém os dados da execução. Os arquivos `.svg` apresentam representações visuais de algumas soluções em formato de tabuleiro.

## Estrutura do projeto

```txt
Projeto-Problema-das-8-Rainhas/
├── main.py
├── README.md
└── outputs/
    ├── solucoes.txt
    ├── estatisticas.txt
    └── imagens/
        ├── solucao_1.svg
        ├── solucao_2.svg
        ├── solucao_3.svg
        ├── solucao_4.svg
        └── solucao_5.svg
```

## Uso de Inteligência Artificial Generativa

Durante o desenvolvimento deste projeto, foi utilizada ferramenta de Inteligência Artificial Generativa para apoio na organização da solução, revisão da explicação do algoritmo, estruturação do código e preparação do material textual.

Ferramenta utilizada: ChatGPT, modelo GPT-5.5 Thinking, da OpenAI.

Finalidade do uso: apoio na concepção da solução, redação explicativa, organização do projeto, revisão da implementação e estruturação do material de apresentação.

O conteúdo final, a implementação, a validação dos resultados e a responsabilidade pela entrega são do autor.
