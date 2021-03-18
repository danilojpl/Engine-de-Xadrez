import chess
import random
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
    # legal_moves = self.board.legal_moves
    # return legal_moves

  def make_move(self, move):
    self.board.push(move)
    self.set_board_array()

  def draw_board(self):
    print('\n')
    print(self.board)
  
  def calc_utility (self, player_color):
    board_array = self.board_array
    return controled_squares_heuristic(board_array, player_color)

  #Daqui pra baixo é so gameplay
  def start_game(self):
    coin = ['heads', 'tails']
    coin_side = random.choice(coin)

    if coin_side == 'heads':
        print("\n")
        print("Você jogará com as peças brancas!")
        self.draw_board()
        self.game_interaction_menu()

    else:
        print("\n")
        print("Você jogará com as peças pretas!")
        self.bot_move() 
  
  def human_move(self): 
    if not self.verify_game_over():
      self.verify_check()

      movement = input("Faça sua jogada: ")
      if self.move_is_valid(movement): 
        # if move in moves:
        self.make_move(chess.Move.from_uci(movement))
        self.draw_board()
        self.bot_move()
      else: 
        print("Jogada Invalida!")
        self.show_moves()
        self.human_move()

  
  def bot_move(self): 
    moves = self.get_next_moves()

    # Aplicar heuristica
    if not self.verify_game_over():
      self.verify_check()
      self.make_move(moves[0])
      print("\n")
      print("Jogada do adversário: ", moves[0])
      self.draw_board()
      self.game_interaction_menu()

  def show_moves(self):
    print("Jogadas disponíveis:")
    moves = self.get_next_moves()
    for move in moves: 
      print(move)
    return moves

  def move_is_valid(self, movement):
    moves = self.get_next_moves()
    
    for move in moves:
      if str(move) == movement:
        return True

    print("Jogada inválida. Lista de jogadas disponíveis:")
    return False


  def game_interaction_menu(self): 
    print("""
1. Fazer Jogada 
2. Mostrar jogadas disponíveis
3. Render-se.
4. Sair.
    """)

    option = input()

    if option == "1":
      self.human_move()
    elif option == "2":
      self.show_moves()
      self.human_move()
    elif option == "3":
      print("Derrota. GGs")
      self.board.reset()
      print("Iniciando novo jogo.")
      self.start_game()
    elif option == "4":
      exit()
    else:
      print("opcao invalida")
      self.game_interaction_menu()

  def verify_game_over(self):
    
    if self.board.is_game_over():
      game_status = "Game Over!"

      if self.board.is_checkmate():
        print(game_status + " CHECKMATE")
        if self.board.turn == False:
          print("Vitória das peças brancas!")
        elif self.board.turn == True:
          print("Vitória das peças pretas!")
      
      if self.board.is_stalemate():
        print(game_status + " EMPATE: Rei afogado. Não há mais movimentos válidos (STALEMATE)")
      
      if self.board.is_insufficient_material(): 
        print(game_status + " EMPATE: Não há possibilidades de vitória. (INSUFFICIENT MATERIAL)")
      
      if self.board.is_fivefold_repetition():
        print(game_status + " EMPATE: O jogo repetiu as mesmas jogadas muitas vezes. (FIVEFOLD REPETITION)")
      
      return True

    else:
      print("A partida continua!")
      return False

  def verify_check(self):
    if self.board.is_check():
      if self.board.turn == False:
        print("Lado preto está em check!")
      elif self.board.turn == True:
        print("Lado branco está em check!")
