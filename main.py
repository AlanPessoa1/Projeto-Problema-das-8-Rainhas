def imprimir_tabuleiro(solucao):
    """
    Imprime uma solução no formato de tabuleiro.

    A solução é uma lista em que:
    - o índice representa a linha;
    - o valor representa a coluna onde a rainha está naquela linha.

    Exemplo:
    [0, 4, 7, 5, 2, 6, 1, 3]
    significa:
    linha 0 -> coluna 0
    linha 1 -> coluna 4
    linha 2 -> coluna 7
    ...
    """

    n = len(solucao)

    for linha in range(n):
        for coluna in range(n):
            if solucao[linha] == coluna:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

    print()


def resolver_n_rainhas(n):
    """
    Resolve o problema das N Rainhas usando backtracking.

    Retorna uma lista contendo todas as soluções encontradas.
    """

    solucoes = []

    colunas_ocupadas = set()
    diagonais_principais_ocupadas = set()
    diagonais_secundarias_ocupadas = set()

    tabuleiro = [-1] * n

    def backtracking(linha):
        """
        Tenta posicionar uma rainha na linha atual.

        Se conseguir posicionar uma rainha em todas as linhas,
        uma solução completa foi encontrada.
        """

        if linha == n:
            solucoes.append(tabuleiro.copy())
            return

        for coluna in range(n):
            diagonal_principal = linha - coluna
            diagonal_secundaria = linha + coluna

            posicao_invalida = (
                coluna in colunas_ocupadas
                or diagonal_principal in diagonais_principais_ocupadas
                or diagonal_secundaria in diagonais_secundarias_ocupadas
            )

            if posicao_invalida:
                continue

            # Escolha: posiciona a rainha
            tabuleiro[linha] = coluna
            colunas_ocupadas.add(coluna)
            diagonais_principais_ocupadas.add(diagonal_principal)
            diagonais_secundarias_ocupadas.add(diagonal_secundaria)

            # Exploração: tenta resolver a próxima linha
            backtracking(linha + 1)

            # Desfazer escolha: remove a rainha e tenta outra coluna
            tabuleiro[linha] = -1
            colunas_ocupadas.remove(coluna)
            diagonais_principais_ocupadas.remove(diagonal_principal)
            diagonais_secundarias_ocupadas.remove(diagonal_secundaria)

    backtracking(0)

    return solucoes


def main():
    n = 8
    solucoes = resolver_n_rainhas(n)

    print(f"Problema das {n} Rainhas")
    print(f"Total de soluções encontradas: {len(solucoes)}")
    print()

    for indice, solucao in enumerate(solucoes, start=1):
        print(f"Solução {indice}:")
        imprimir_tabuleiro(solucao)


if __name__ == "__main__":
    main()