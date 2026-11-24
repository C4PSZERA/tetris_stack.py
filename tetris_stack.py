"""
Tetris Stack - CLI Edition
Empilhe blocos escolhendo a coluna. Linha completa some e vale pontos.
"""

LARGURA = 6
ALTURA = 8
VAZIO = "."
BLOCO = "#"
PONTOS_POR_LINHA = 100


def criar_grid():
    return [[VAZIO] * LARGURA for _ in range(ALTURA)]


def desenhar(grid, pontos):
    print("\n" + "=" * (LARGURA * 2 + 3))
    print(f" Pontos: {pontos}")
    print("=" * (LARGURA * 2 + 3))
    for linha in grid:
        print("| " + " ".join(linha) + " |")
    print("+" + "-" * (LARGURA * 2 + 1) + "+")
    print("  " + " ".join(str(c) for c in range(LARGURA)))


def soltar_bloco(grid, coluna):
    """Aplica a gravidade: o bloco cai até a posição livre mais baixa.
    Retorna False se a coluna já estiver cheia."""
    for linha in range(ALTURA - 1, -1, -1):
        if grid[linha][coluna] == VAZIO:
            grid[linha][coluna] = BLOCO
            return True
    return False


def limpar_linhas(grid):
    """Remove linhas completas e adiciona linhas vazias no topo."""
    restantes = [linha for linha in grid if VAZIO in linha]
    removidas = ALTURA - len(restantes)
    novas = [[VAZIO] * LARGURA for _ in range(removidas)]
    grid[:] = novas + restantes
    return removidas


def jogar():
    grid = criar_grid()
    pontos = 0
    print("🧱 TETRIS STACK - CLI EDITION")
    print(f"Escolha uma coluna de 0 a {LARGURA - 1} ou digite S para sair.")

    while True:
        desenhar(grid, pontos)
        entrada = input("Coluna: ").strip().upper()

        if entrada == "S":
            print(f"\nAté a próxima! Pontuação final: {pontos}")
            break

        if not entrada.isdigit() or not 0 <= int(entrada) < LARGURA:
            print(f"⚠️ Entrada inválida. Digite um número de 0 a {LARGURA - 1}.")
            continue

        if not soltar_bloco(grid, int(entrada)):
            desenhar(grid, pontos)
            print(f"\n💀 GAME OVER! A coluna {entrada} chegou ao topo.")
            print(f"Pontuação final: {pontos}")
            break

        linhas = limpar_linhas(grid)
        if linhas:
            pontos += linhas * PONTOS_POR_LINHA
            print(f"✨ {linhas} linha(s) completa(s)! +{linhas * PONTOS_POR_LINHA} pontos")


if __name__ == "__main__":
    jogar()
