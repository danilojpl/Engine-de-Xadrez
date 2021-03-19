import chess

from __config import HEURISTICS, PIECES_WEIGHTS

def checkmate_heuristic (board, player_color):
  points = 1 if board.is_checkmate else 0
  
  return (points * HEURISTICS['check_mate'])
