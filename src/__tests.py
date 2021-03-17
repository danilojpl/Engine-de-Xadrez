import chess

from left_pieces_heuristic import left_pieces_heuristic
from controled_squares_heuristic import controled_squares_heuristic
from pieces_to_capture_heuristic import pieces_to_capture_heuristic

from Game import Game
from __config import TREE_MAX_DEPT, SQUARES_WEIGHTS, HEURISTICS, PIECES_WEIGHTS

game = Game()

# DEIXAR O TABULEIRO EM UM ESTADO ALEATÓRIO E CONTROLADO:
for x in range(50):
  game.make_move(game.get_next_moves()[1])

# TESTANDO A REPRESENTAÇÃO EM MATRIZ DO TABULEIRO
piece = game.board_array[7][3]
assert piece.symbol() == 'Q'
assert piece.color == True
print('✅ game.boad_array')

# TESTANDO O DICIONÁRIO DE PONTUAÇÃO DAS PEÇAS:
piece_points = PIECES_WEIGHTS[piece.piece_type]
assert piece_points == 9
print('✅ PIECES_WEIGHTS')

# TESTANDO HEURÍSTICA DE PEÇAS NO TABULEIRO
white_left_pieces_utility = left_pieces_heuristic(game.board_array, chess.WHITE)
black_left_pieces_utility = left_pieces_heuristic(game.board_array, chess.BLACK)
assert white_left_pieces_utility == 46
assert black_left_pieces_utility == 44
print('✅ left_pieces_heuristic')
# print(f"\nPontos da heurística de peças restantes para o jogador BRANCO = {left_pieces_utility}")

# TESTANDO HEURÍSTICA DE CASAS CONTROLADAS
white_controled_squares_utility = controled_squares_heuristic(game.board_array, chess.WHITE)
black_controled_squares_utility = controled_squares_heuristic(game.board_array, chess.BLACK)
assert white_controled_squares_utility == 43
assert black_controled_squares_utility == 51
print('✅ controled_squares_heuristic')

# TESTANDO HEURÍSTICA DE PEÇAS A SEREM CAPTURADAS
white_pieces_to_capture_utility = pieces_to_capture_heuristic(game.board_array, chess.WHITE)
black_pieces_to_capture_utility = pieces_to_capture_heuristic(game.board_array, chess.BLACK)
assert white_pieces_to_capture_utility == 1
assert black_pieces_to_capture_utility == 3
print('✅ pieces_to_capture_heuristic')
