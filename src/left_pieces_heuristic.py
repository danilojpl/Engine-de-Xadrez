import chess

from __config import HEURISTICS, PIECES_WEIGHTS

def left_pieces_heuristic (board_array, player_color):
  points = 0

  for row in board_array:
    for piece in row:
      if player_color == piece.color:
        points += PIECES_WEIGHTS[abs(piece.piece_type)]
  
  return (points * HEURISTICS['left_pieces'])
