import chess
from Game import NullPiece

# Tamanho máximo da árvore
TREE_MAX_DEPT = 6

# Peso das casas
SQUARES_WEIGHTS = {
  "border": 1,
  "middle": 1,
  "center": 1
}

# Peso das heurísticas
HEURISTICS = {
  "left_pieces": 1,
  "unprotected_pieces": 1,
  "check_mate": 1,
  "square_control": 1,
  "draw": 1
}

# Peso das peças
PIECES_WEIGHTS = {
  NullPiece().piece_type: 0,
  chess.PAWN: 1,
  chess.KNIGHT: 3,
  chess.BISHOP: 3,
  chess.ROOK: 5,
  chess.QUEEN: 9,
  chess.KING: 10
}
