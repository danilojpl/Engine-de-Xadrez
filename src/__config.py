import chess

# Peça nula
NULL_PIECE = {
  "piece_type": 0,
  "symbol": '.',
  "color": False
}

# Tamanho máximo da árvore
TREE_MAX_DEPT = 2

# Peso das casas
SQUARES_WEIGHTS = {
  "border": 1,
  "middle": 2,
  "center": 3
}

# Peso das heurísticas
HEURISTICS = {
  "left_pieces": 1,
  "pieces_to_capture": 1,
  "check_mate": 1,
  "square_control": 1,
  "draw": 1
}

# Peso das peças
PIECES_WEIGHTS = {
  NULL_PIECE['piece_type']: 0,
  chess.PAWN: 1,
  chess.KNIGHT: 3,
  chess.BISHOP: 3,
  chess.ROOK: 5,
  chess.QUEEN: 9,
  chess.KING: 10
}
