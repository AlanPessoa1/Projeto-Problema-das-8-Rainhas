from pathlib import Path


def resolver_n_rainhas(n):
    """
    Resolve o problema das N Rainhas usando backtracking.

    Retorna:
    - lista com todas as soluções encontradas;
    - dicionário com estatísticas da execução.
    """

    solucoes = []

    estatisticas = {
        "chamadas_recursivas": 0,
        "tentativas_de_posicionamento": 0,
        "posicoes_validas_testadas": 0,
        "retrocessos": 0,
    }

    colunas_ocupadas = set()
    diagonais_principais_ocupadas = set()
    diagonais_secundarias_ocupadas = set()

    tabuleiro = [-1] * n

    def backtracking(linha):
        estatisticas["chamadas_recursivas"] += 1

        if linha == n:
            solucoes.append(tabuleiro.copy())
            return

        for coluna in range(n):
            estatisticas["tentativas_de_posicionamento"] += 1

            diagonal_principal = linha - coluna
            diagonal_secundaria = linha + coluna

            posicao_invalida = (
                coluna in colunas_ocupadas
                or diagonal_principal in diagonais_principais_ocupadas
                or diagonal_secundaria in diagonais_secundarias_ocupadas
            )

            if posicao_invalida:
                continue

            estatisticas["posicoes_validas_testadas"] += 1

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

            estatisticas["retrocessos"] += 1

    backtracking(0)

    return solucoes, estatisticas


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


def salvar_solucoes_em_txt(solucoes, estatisticas, caminho_arquivo):
    """
    Salva todas as soluções encontradas em um arquivo de texto.
    """

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("Problema das 8 Rainhas\n")
        arquivo.write(f"Total de soluções encontradas: {len(solucoes)}\n\n")

        arquivo.write("Estatísticas da execução:\n")
        arquivo.write(f"Chamadas recursivas: {estatisticas['chamadas_recursivas']}\n")
        arquivo.write(
            f"Tentativas de posicionamento: {estatisticas['tentativas_de_posicionamento']}\n"
        )
        arquivo.write(
            f"Posições válidas testadas: {estatisticas['posicoes_validas_testadas']}\n"
        )
        arquivo.write(f"Retrocessos realizados: {estatisticas['retrocessos']}\n\n")

        for indice, solucao in enumerate(solucoes, start=1):
            arquivo.write(f"Solução {indice}:\n")
            arquivo.write(solucao_para_texto(solucao))
            arquivo.write("\n\n")


def gerar_svg_tabuleiro(solucao, caminho_arquivo):
    """
    Gera uma imagem SVG representando uma solução do problema.
    """

    n = len(solucao)
    tamanho_casa = 80
    tamanho_total = n * tamanho_casa

    partes_svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{tamanho_total}" height="{tamanho_total}" viewBox="0 0 {tamanho_total} {tamanho_total}">',
        '<rect width="100%" height="100%" fill="white"/>',
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


def salvar_estatisticas(estatisticas, total_solucoes, caminho_arquivo):
    """
    Salva um resumo separado das estatísticas da execução.
    """

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("Estatísticas da execução\n\n")
        arquivo.write(f"Total de soluções encontradas: {total_solucoes}\n")
        arquivo.write(f"Chamadas recursivas: {estatisticas['chamadas_recursivas']}\n")
        arquivo.write(
            f"Tentativas de posicionamento: {estatisticas['tentativas_de_posicionamento']}\n"
        )
        arquivo.write(
            f"Posições válidas testadas: {estatisticas['posicoes_validas_testadas']}\n"
        )
        arquivo.write(f"Retrocessos realizados: {estatisticas['retrocessos']}\n")


def main():
    n = 8

    pasta_outputs = Path("outputs")
    pasta_imagens = pasta_outputs / "imagens"

    pasta_outputs.mkdir(exist_ok=True)
    pasta_imagens.mkdir(exist_ok=True)

    solucoes, estatisticas = resolver_n_rainhas(n)

    print(f"Problema das {n} Rainhas")
    print(f"Total de soluções encontradas: {len(solucoes)}")
    print()

    print("Estatísticas da execução:")
    print(f"Chamadas recursivas: {estatisticas['chamadas_recursivas']}")
    print(f"Tentativas de posicionamento: {estatisticas['tentativas_de_posicionamento']}")
    print(f"Posições válidas testadas: {estatisticas['posicoes_validas_testadas']}")
    print(f"Retrocessos realizados: {estatisticas['retrocessos']}")
    print()

    print("Primeira solução encontrada:")
    print(solucao_para_texto(solucoes[0]))

    caminho_txt = pasta_outputs / "solucoes.txt"
    salvar_solucoes_em_txt(solucoes, estatisticas, caminho_txt)

    caminho_estatisticas = pasta_outputs / "estatisticas.txt"
    salvar_estatisticas(estatisticas, len(solucoes), caminho_estatisticas)

    quantidade_imagens = 5

    for indice, solucao in enumerate(solucoes[:quantidade_imagens], start=1):
        caminho_svg = pasta_imagens / f"solucao_{indice}.svg"
        gerar_svg_tabuleiro(solucao, caminho_svg)

    print()
    print(f"Todas as soluções foram salvas em: {caminho_txt}")
    print(f"As estatísticas foram salvas em: {caminho_estatisticas}")
    print(f"{quantidade_imagens} imagens SVG foram geradas em: {pasta_imagens}")


if __name__ == "__main__":
    main()
