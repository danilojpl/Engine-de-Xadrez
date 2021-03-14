import chess

from Game import Game
from __config import TREE_MAX_DEPT, SQUARES_WEIGHTS, HEURISTICS, PIECES_WEIGHTS
from heuristics import left_pieces

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

# SELECIONAR UMA PEÇA DA 8ª LINHA (DE CIMA PARA BAIXO) E 5ª COLUNA (DA ESQUERDA PARA A DIREITA):
piece = game.board_array[7][4]
print(f"\nPeça em {8}x{5}: {piece.symbol()} ({chess.COLOR_NAMES[piece.color]} {chess.PIECE_NAMES[piece.piece_type]})")

# PEGAR A PONTUAÇÃO DA PEÇA (0 NO CASO DA CASA ESTAR VAZIA):
points = PIECES_WEIGHTS[piece.piece_type]
print(f"Pontos dessa peça: {points}")

# CALCULAR UTILIDADE DO TABULEIRO CONSIDERANDO A QUANTIDADE DE PEÇAS DE UMA COR
left_pieces_utility = left_pieces(array, chess.WHITE)
print(f"\nPontos da heurística de peças restantes para o jogador BRANCO = {left_pieces_utility}")
