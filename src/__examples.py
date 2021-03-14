import chess

from __config import TREE_MAX_DEPT, SQUARES_WEIGHTS, HEURISTICS, PIECES_WEIGHTS
from Game import Game

# INICIAR UM TABULEIRO:
game = Game()

# PRÓXIMOS MOVIMENTOS POSSÍVEIS:
moves = game.get_next_moves()

# DESENHAR O TABULEIRO (NO CONSOLE):
print('Tabuleiro:')
game.draw_board()

# REALIZAR UM MOVIMENTO:
game.make_move(moves[0])

# ACESSAR A REPRESENTAÇÃO EM ARRAY DE 2 DIMENSÕES DO TABULEIRO:
array = game.board_array
print('\nRepresentação em array:')
for r in array:
    for c in r:
      print(c, end = " ")
    print()

# SELECIONAR UMA PEÇA DA 1ª LINHA (DE BAIXO PARA CIMA) E 2ª COLUNA (DA ESQUERDA PARA A DIREITA):
piece = game.board_array[0][1]
print(f"\nPeça em {1}x{2}: {piece} ({chess.PIECE_NAMES[piece]})")

# PEGAR A PONTUAÇÃO DA PEÇA (0 NO CASO DA CASA ESTAR VAZIA):
points = PIECES_WEIGHTS[piece]
print(f"Pontos: {points}")
