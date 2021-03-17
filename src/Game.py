import chess
from __config import NULL_PIECE
from controled_squares_heuristic import controled_squares_heuristic

class NullPiece(chess.Piece):
  def __init__(self):
    self.piece_type = NULL_PIECE['piece_type']
    self.symbol = NULL_PIECE['symbol']
    self.color = NULL_PIECE['color']

  def __str__(self):
    return self.symbol

class Game:
  def __init__(self):
    self.board = chess.Board()
    self.set_board_array()

  def clone_board(self):
    return self.board

  def set_board_array(self):
    board_array = []
    row_array = []

    for square in chess.SQUARES:
      piece = self.board.piece_at(square)

      if piece:
        row_array.append(piece)
      else:
        row_array.append(NullPiece())

      if square % 8 == 7:
        board_array.append(row_array)
        row_array = []
    
    self.board_array = board_array[::-1]

  def get_next_moves(self):
    return [move for move in self.board.legal_moves]

  def make_move(self, move):
    self.board.push(move)
    self.set_board_array()

  def draw_board(self):
    print('\n')
    print(self.board)
  
  def calc_utility (self, player_color):
    board_array = self.board_array
    return controled_squares_heuristic(board_array, player_color)




