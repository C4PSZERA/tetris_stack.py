import random
import os

# Configurações do Jogo
LARGURA = 6
ALTURA = 10
VAZIO = "."
BLOCO = "█"

def criar_grid():
    return [[VAZIO for _ in range(LARGURA)] for _ in range(ALTURA)]

def desenhar_grid(grid, pontos, proxima_peca):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n🎮 TETRIS STACK - TEMA 3: CLI 🎮")
    print(f"Pontuação: {pontos} | Próxima: {proxima_peca}")
    print("=" * (LARGURA * 3 + 2))
    
    for linha in grid:
        print("| " + "  ".join(linha) + " |")
        
    print("=" * (LARGURA * 3 + 2))
    print("  " + "  ".join([str(i) for i in range(LARGURA)])) # Números das colunas

def soltar_peca(grid, coluna):
    # Verifica de baixo para cima onde está o primeiro espaço vazio
    for i in range(ALTURA - 1, -1, -1):
        if grid[i][coluna] == VAZIO:
            grid[i][coluna] = BLOCO
            return True # Peça colocada com sucesso
    return False # Coluna cheia (Game Over nessa coluna)

def verificar_linhas(grid):
    linhas_completas = 0
    linhas_para_manter = []
    
    # Identifica linhas que não estão cheias
    for linha in grid:
        if VAZIO in linha:
            linhas_para_manter.append(linha)
        else:
            linhas_completas += 1
            
    # Adiciona novas linhas vazias no topo para compensar as removidas
    while len(linhas_para_manter) < ALTURA:
        linhas_para_manter.insert(0, [VAZIO for _ in range(LARGURA)])
        
    # Atualiza o grid
    for i in range(ALTURA):
        grid[i] = linhas_para_manter[i]
        
    return linhas_completas

def main():
    grid = criar_grid()
    pontos = 0
    jogando = True
    
    # Tipos de peças simplificadas para o desafio (1 bloco, 2 blocos verticais)
    # Aqui simula-se apenas a lógica de "Stack" (empilhar)
    
    while jogando:
        # Gera uma "peça" (aqui simplificada como um bloco único para lógica de stack)
        # Para expandir o "Tema 3", você pode alterar isso para peças de tamanhos diferentes
        proxima = BLOCO 
        
        desenhar_grid(grid, pontos, proxima)
        
        try:
            coluna_escolhida = input("\nEscolha a coluna (0-5) ou 'S' para sair: ").strip().lower()
            
            if coluna_escolhida == 's':
                break
                
            coluna = int(coluna_escolhida)
            
            if 0 <= coluna < LARGURA:
                if not soltar_peca(grid, coluna):
                    print("\n❌ Coluna cheia! Fim de Jogo.")
                    jogando = False
                else:
                    linhas_limpas = verificar_linhas(grid)
                    if linhas_limpas > 0:
                        pontos += (linhas_limpas * 100)
                        print(f"✨ Linha Completa! +{linhas_limpas*100} pts")
            else:
                print("⚠️ Coluna inválida!")
                
        except ValueError:
            print("⚠️ Entrada inválida! Digite um número.")

    print(f"\n🏁 Jogo Encerrado! Pontuação Final: {pontos}")

if __name__ == "__main__":
    main()
