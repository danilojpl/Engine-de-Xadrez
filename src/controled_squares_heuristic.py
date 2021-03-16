import chess
from __config import NULL_PIECE, SQUARES_WEIGHTS, HEURISTICS

def square_is_in_board(row, col):
  return row >= 0 and row <= 7 and col >= 0 and col <= 7

def get_square_weight(row, col):
  if row == 0 or row == 1 or row == 6 or row == 7:
    square_weight = SQUARES_WEIGHTS['border']
  elif row == 2 or row == 5 or col == 0 or col == 1 or col == 2 or col == 5 or col == 6 or col == 7:
    square_weight = SQUARES_WEIGHTS['middle']
  else:
    square_weight = SQUARES_WEIGHTS['center']

  return square_weight

def pawn_controled_squares (board_array, pawn_square_r, pawn_square_c, player_color):
  controled_squares = 0

  movement_r = pawn_square_r + (-1 if player_color else 1)
  movement_c_1 = pawn_square_c - 1
  movement_c_2 = pawn_square_c + 1

  if (square_is_in_board(movement_r, movement_c_1) and
      board_array[movement_r][movement_c_1].piece_type == NULL_PIECE['piece_type']):
    controled_squares += get_square_weight(movement_r, movement_c_1)

  if (square_is_in_board(movement_r, movement_c_2) and
      board_array[movement_r][movement_c_2].piece_type == NULL_PIECE['piece_type']):
    controled_squares += get_square_weight(movement_r, movement_c_2)

  return controled_squares

def knight_controled_squares (board_array, knight_square_r, knight_square_c):
  controled_squares = 0
  possible_moves = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]

  for move_r, move_c in possible_moves:
    check_r = knight_square_r + move_r
    check_c = knight_square_c + move_c

    if (square_is_in_board(check_r, check_c) and
        board_array[check_r][check_c].piece_type == NULL_PIECE['piece_type']):
      controled_squares += get_square_weight(check_r, check_c)

  return controled_squares

def check_while_moving (board_array, initial_r, initial_c, move_r, move_c):
  points = 0
  check_r = initial_r
  check_c = initial_c

  i = True

  while i:
    check_r += move_r
    check_c += move_c

    if (square_is_in_board(check_r, check_c) and
        board_array[check_r][check_c].piece_type == NULL_PIECE['piece_type']):
      points += get_square_weight(check_r, check_c)
    else:
      i = False

  return points

def bishop_controled_squares (board_array, bishop_square_r, bishop_square_c):
  controled_squares = 0

  controled_squares += check_while_moving(board_array, bishop_square_r, bishop_square_c, 1, 1)
  controled_squares += check_while_moving(board_array, bishop_square_r, bishop_square_c, 1, -1)
  controled_squares += check_while_moving(board_array, bishop_square_r, bishop_square_c, -1, 1)
  controled_squares += check_while_moving(board_array, bishop_square_r, bishop_square_c, -1, -1)

  return controled_squares

def rook_controled_squares (board_array, rook_square_r, rook_square_c):
  controled_squares = 0

  controled_squares += check_while_moving(board_array, rook_square_r, rook_square_c, 1, 0)
  controled_squares += check_while_moving(board_array, rook_square_r, rook_square_c, 0, 1)
  controled_squares += check_while_moving(board_array, rook_square_r, rook_square_c, -1, 0)
  controled_squares += check_while_moving(board_array, rook_square_r, rook_square_c, 0, -1)

  return controled_squares

def queen_controled_squares (board_array, queen_square_r, queen_square_c):
  controled_squares = 0

  controled_squares += bishop_controled_squares(board_array, queen_square_r, queen_square_c)
  controled_squares += rook_controled_squares(board_array, queen_square_r, queen_square_c)

  return controled_squares

def king_controled_squares (board_array, king_square_r, king_square_c):
  controled_squares = 0

  possible_moves = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

  for move_r, move_c in possible_moves:
    check_r = king_square_r + move_r
    check_c = king_square_c + move_c

    if (square_is_in_board(check_r, check_c) and
        board_array[check_r][check_c].piece_type == NULL_PIECE['piece_type']):
      controled_squares += get_square_weight(check_r, check_c)

  return controled_squares

def controled_squares_heuristic (board_array, player_color):
  points = 0

  for row, pieces_row in enumerate(board_array):
    for col, piece in enumerate(pieces_row):
      if player_color == piece.color:
        if piece.piece_type == chess.PAWN:
          points += pawn_controled_squares(board_array, row, col, player_color)
        if piece.piece_type == chess.KNIGHT:
          points += knight_controled_squares(board_array, row, col)
        if piece.piece_type == chess.BISHOP:
          points += bishop_controled_squares(board_array, row, col)
        if piece.piece_type == chess.ROOK:
          points += rook_controled_squares(board_array, row, col)
        if piece.piece_type == chess.QUEEN:
          points += queen_controled_squares(board_array, row, col)
        if piece.piece_type == chess.KING:
          points += king_controled_squares(board_array, row, col)
          
        
  return (points * HEURISTICS['square_control'])
