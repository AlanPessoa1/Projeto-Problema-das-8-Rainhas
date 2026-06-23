# Problema das 8 Rainhas

Este projeto apresenta uma solução para o Problema das 8 Rainhas utilizando a técnica de **backtracking**.

O objetivo do problema é posicionar 8 rainhas em um tabuleiro de xadrez 8x8 de forma que nenhuma rainha ataque outra. Assim, duas rainhas não podem estar na mesma linha, na mesma coluna ou na mesma diagonal.

## Técnica utilizada

A técnica utilizada foi o **backtracking**, uma estratégia algorítmica baseada em tentativa e erro controlado.

O algoritmo posiciona uma rainha por linha. Para cada linha, ele testa as colunas disponíveis e verifica se a posição escolhida é válida. Caso a posição seja válida, o algoritmo avança para a próxima linha. Caso o caminho não leve a uma solução completa, a escolha é desfeita e uma nova posição é testada.

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

## Como executar

Para executar o projeto, utilize:

```bash
python main.py
```

O programa irá:

1. resolver o Problema das 8 Rainhas;
2. exibir no terminal a primeira solução encontrada;
3. salvar todas as soluções no arquivo `outputs/solucoes.txt`;
4. gerar imagens em SVG de algumas soluções na pasta `outputs/imagens`.

## Resultado

Para o caso clássico com 8 rainhas, o algoritmo encontra:

```txt
Total de soluções encontradas: 92
```

## Arquivos gerados

Após a execução, são gerados os seguintes arquivos:

```txt
outputs/solucoes.txt
outputs/imagens/solucao_1.svg
outputs/imagens/solucao_2.svg
outputs/imagens/solucao_3.svg
outputs/imagens/solucao_4.svg
outputs/imagens/solucao_5.svg
```

O arquivo `solucoes.txt` contém todas as soluções encontradas. Os arquivos `.svg` apresentam representações visuais de algumas soluções em formato de tabuleiro.

## Uso de Inteligência Artificial Generativa

Durante o desenvolvimento deste projeto, foi utilizada ferramenta de Inteligência Artificial Generativa para apoio na organização da solução, revisão da explicação do algoritmo, estruturação do código e preparação do material textual.

O conteúdo final, a implementação e a validação da solução são de responsabilidade do autor.
