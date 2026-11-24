# 🧱 Tetris Stack: CLI Edition

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Sem dependências](https://img.shields.io/badge/dependências-nenhuma-2ea44f?style=flat-square)

Lógica de empilhamento inspirada no Tetris, rodando direto no terminal.

## 📝 Sobre o projeto

Desafio de lógica de programação (Tema 3: **eficiência e minimalismo**). O foco é a lógica do jogo pura, sem interface gráfica e sem bibliotecas externas:

- **Grid 2D:** uma matriz de 6 colunas × 8 linhas
- **Gravidade:** o bloco cai até a posição livre mais baixa da coluna
- **Limpeza de linhas:** linha completa é removida e as de cima descem
- **Colisão / game over:** soltar um bloco numa coluna cheia encerra o jogo

## 🎮 Como jogar

```bash
git clone https://github.com/C4PSZERA/tetris_stack.py.git
cd tetris_stack.py
python tetris_stack.py
```

| Comando | Ação |
|---|---|
| `0` a `5` + `Enter` | Solta um bloco na coluna |
| `S` | Sai do jogo |

Cada linha completa vale **100 pontos**.

```
=================
 Pontos: 100
=================
| . . . . . . |
| . . . . . . |
| . . . . . . |
| . . . . . . |
| . . . . . . |
| . . . . . . |
| . . # . . . |
| # . # # . # |
+-------------+
  0 1 2 3 4 5
```

## 💡 Próximas ideias

- [ ] Peças com formatos diferentes (L, T, quadrado)
- [ ] Ranking de pontuação salvo em arquivo

---

Feito por [C4PSZERA](https://github.com/C4PSZERA) 🦫
