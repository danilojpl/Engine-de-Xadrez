import chess

from __config import HEURISTICS, PIECES_WEIGHTS

def checkmate_heuristic (board, player_color):
  points = 1 if board.is_checkmate and board.turn == player_color else 0
  
  return (points * HEURISTICS['check_mate'])
