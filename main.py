from pathlib import Path


def resolver_n_rainhas(n):
    """
    Resolve o problema das N Rainhas usando backtracking.

    Retorna uma lista com todas as soluções encontradas.
    Cada solução é uma lista em que:
    - o índice representa a linha;
    - o valor representa a coluna onde a rainha está.
    """

    solucoes = []

    colunas_ocupadas = set()
    diagonais_principais_ocupadas = set()
    diagonais_secundarias_ocupadas = set()

    tabuleiro = [-1] * n

    def backtracking(linha):
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

            # Escolha
            tabuleiro[linha] = coluna
            colunas_ocupadas.add(coluna)
            diagonais_principais_ocupadas.add(diagonal_principal)
            diagonais_secundarias_ocupadas.add(diagonal_secundaria)

            # Exploração
            backtracking(linha + 1)

            # Desfazer escolha
            tabuleiro[linha] = -1
            colunas_ocupadas.remove(coluna)
            diagonais_principais_ocupadas.remove(diagonal_principal)
            diagonais_secundarias_ocupadas.remove(diagonal_secundaria)

    backtracking(0)

    return solucoes


def solucao_para_texto(solucao):
    """
    Converte uma solução em uma representação textual do tabuleiro.
    """

    n = len(solucao)
    linhas = []

    for linha in range(n):
        linha_tabuleiro = []

        for coluna in range(n):
            if solucao[linha] == coluna:
                linha_tabuleiro.append("Q")
            else:
                linha_tabuleiro.append(".")

        linhas.append(" ".join(linha_tabuleiro))

    return "\n".join(linhas)


def salvar_solucoes_em_txt(solucoes, caminho_arquivo):
    """
    Salva todas as soluções encontradas em um arquivo de texto.
    """

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Total de soluções encontradas: {len(solucoes)}\n\n")

        for indice, solucao in enumerate(solucoes, start=1):
            arquivo.write(f"Solução {indice}:\n")
            arquivo.write(solucao_para_texto(solucao))
            arquivo.write("\n\n")


def gerar_svg_tabuleiro(solucao, caminho_arquivo):
    """
    Gera uma imagem SVG representando uma solução do problema.

    SVG é um formato de imagem vetorial que pode ser aberto no navegador
    e usado em slides/documentos.
    """

    n = len(solucao)
    tamanho_casa = 80
    tamanho_total = n * tamanho_casa

    partes_svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{tamanho_total}" height="{tamanho_total}" viewBox="0 0 {tamanho_total} {tamanho_total}">',
        '<rect width="100%" height="100%" fill="white"/>'
    ]

    for linha in range(n):
        for coluna in range(n):
            x = coluna * tamanho_casa
            y = linha * tamanho_casa

            cor = "#f0d9b5" if (linha + coluna) % 2 == 0 else "#b58863"

            partes_svg.append(
                f'<rect x="{x}" y="{y}" width="{tamanho_casa}" height="{tamanho_casa}" fill="{cor}" stroke="black"/>'
            )

            if solucao[linha] == coluna:
                centro_x = x + tamanho_casa / 2
                centro_y = y + tamanho_casa / 2 + 12

                partes_svg.append(
                    f'<text x="{centro_x}" y="{centro_y}" text-anchor="middle" font-size="54" font-family="Arial">♛</text>'
                )

    partes_svg.append("</svg>")

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("\n".join(partes_svg))


def main():
    n = 8

    pasta_outputs = Path("outputs")
    pasta_imagens = pasta_outputs / "imagens"

    pasta_outputs.mkdir(exist_ok=True)
    pasta_imagens.mkdir(exist_ok=True)

    solucoes = resolver_n_rainhas(n)

    print(f"Problema das {n} Rainhas")
    print(f"Total de soluções encontradas: {len(solucoes)}")
    print()

    print("Primeira solução encontrada:")
    print(solucao_para_texto(solucoes[0]))

    caminho_txt = pasta_outputs / "solucoes.txt"
    salvar_solucoes_em_txt(solucoes, caminho_txt)

    print()
    print(f"Todas as soluções foram salvas em: {caminho_txt}")

    quantidade_imagens = 5

    for indice, solucao in enumerate(solucoes[:quantidade_imagens], start=1):
        caminho_svg = pasta_imagens / f"solucao_{indice}.svg"
        gerar_svg_tabuleiro(solucao, caminho_svg)

    print(f"{quantidade_imagens} imagens SVG foram geradas em: {pasta_imagens}")


if __name__ == "__main__":
    main()