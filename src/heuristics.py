from __config import TREE_MAX_DEPT, SQUARES_WEIGHTS, HEURISTICS, PIECES_WEIGHTS

def left_pieces (board_array, player_color):
  points = 0

  for row in board_array:
    for piece in row:
      if player_color == piece.color:
        points += abs(PIECES_WEIGHTS[piece.piece_type])
  
  return (points * HEURISTICS['left_pieces'])
