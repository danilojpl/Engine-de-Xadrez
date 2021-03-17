import chess
from __config import NULL_PIECE, PIECES_WEIGHTS, HEURISTICS

def square_is_in_board(row, col):
  return row >= 0 and row <= 7 and col >= 0 and col <= 7

def pieces_pawn_can_capture (board_array, pawn_square_r, pawn_square_c, player_color):
  pieces_points = 0

  movement_r = pawn_square_r + (-1 if player_color else 1)
  movement_c_1 = pawn_square_c - 1
  movement_c_2 = pawn_square_c + 1

  if (square_is_in_board(movement_r, movement_c_1) and
      board_array[movement_r][movement_c_1].color != player_color):
    pieces_points += PIECES_WEIGHTS[board_array[movement_r][movement_c_1].piece_type]

  if (square_is_in_board(movement_r, movement_c_2) and
      board_array[movement_r][movement_c_2].color != player_color):
    pieces_points += PIECES_WEIGHTS[board_array[movement_r][movement_c_2].piece_type]

  return pieces_points

def pieces_knight_can_capture (board_array, knight_square_r, knight_square_c, player_color):
  pieces_points = 0
  possible_moves = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]

  for move_r, move_c in possible_moves:
    check_r = knight_square_r + move_r
    check_c = knight_square_c + move_c

    if (square_is_in_board(check_r, check_c) and
        board_array[check_r][check_c].color != player_color):
      pieces_points += PIECES_WEIGHTS[board_array[check_r][check_c].piece_type]

  return pieces_points

def check_while_moving (player_color, board_array, initial_r, initial_c, move_r, move_c):
  pieces_points = 0

  check_r = initial_r
  check_c = initial_c

  i = True

  while i:
    check_r += move_r
    check_c += move_c

    if (square_is_in_board(check_r, check_c) and
        board_array[check_r][check_c].color != player_color):
      pieces_points += PIECES_WEIGHTS[board_array[check_r][check_c].piece_type]
    else:
      i = False

  return pieces_points

def pieces_bishop_can_capture (board_array, bishop_square_r, bishop_square_c, player_color):
  pieces_points = 0

  pieces_points += check_while_moving(player_color, board_array, bishop_square_r, bishop_square_c, 1, 1)
  pieces_points += check_while_moving(player_color, board_array, bishop_square_r, bishop_square_c, 1, -1)
  pieces_points += check_while_moving(player_color, board_array, bishop_square_r, bishop_square_c, -1, 1)
  pieces_points += check_while_moving(player_color, board_array, bishop_square_r, bishop_square_c, -1, -1)

  return pieces_points

def pieces_rook_can_capture (board_array, rook_square_r, rook_square_c, player_color):
  pieces_points = 0

  pieces_points += check_while_moving(player_color, board_array, rook_square_r, rook_square_c, 1, 0)
  pieces_points += check_while_moving(player_color, board_array, rook_square_r, rook_square_c, 0, 1)
  pieces_points += check_while_moving(player_color, board_array, rook_square_r, rook_square_c, -1, 0)
  pieces_points += check_while_moving(player_color, board_array, rook_square_r, rook_square_c, 0, -1)

  return pieces_points


def pieces_queen_can_capture (board_array, queen_square_r, queen_square_c, player_color):
  pieces_points = 0

  pieces_points += pieces_bishop_can_capture(board_array, queen_square_r, queen_square_c, player_color)
  pieces_points += pieces_rook_can_capture(board_array, queen_square_r, queen_square_c, player_color)

  return pieces_points

def pieces_king_can_capture (board_array, king_square_r, king_square_c, player_color):
  pieces_points = 0
  possible_moves = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

  for move_r, move_c in possible_moves:
    check_r = king_square_r + move_r
    check_c = king_square_c + move_c

    if (square_is_in_board(check_r, check_c) and
        board_array[check_r][check_c].color != player_color):
      pieces_points += PIECES_WEIGHTS[board_array[check_r][check_c].piece_type]

  return pieces_points

def pieces_to_capture_heuristic (board_array, player_color):
  points = 0

  for row, pieces_row in enumerate(board_array):
    for col, piece in enumerate(pieces_row):
      if player_color == piece.color:
        if piece.piece_type == chess.PAWN:
          points += pieces_pawn_can_capture(board_array, row, col, player_color)
        if piece.piece_type == chess.KNIGHT:
          points += pieces_knight_can_capture(board_array, row, col, player_color)
        if piece.piece_type == chess.BISHOP:
          points += pieces_bishop_can_capture(board_array, row, col, player_color)
        if piece.piece_type == chess.ROOK:
          points += pieces_rook_can_capture(board_array, row, col, player_color)
        if piece.piece_type == chess.QUEEN:
          points += pieces_queen_can_capture(board_array, row, col, player_color)
        if piece.piece_type == chess.KING:
          points += pieces_king_can_capture(board_array, row, col, player_color)
          
  return (points * HEURISTICS['pieces_to_capture'])
