from __config import TREE_MAX_DEPT, SQUARES_WEIGHTS, HEURISTICS, PIECES_WEIGHTS
from Game import Game
from minimax import the_best_move
import random

#iniciando o jogo
game = Game()
game.draw_board()

coin = [0, 1]

if random.choice(coin) == 0:
  print("** VOCÊ JOGARÁ COM AS PEÇAS BRANCAS **")
  while True:
    if not game.verify_game_over():
      game.verify_check()
      game = game.human_move()
      game.draw_board()
    else:
      break

    if not game.verify_game_over():
      computer = the_best_move(game,TREE_MAX_DEPT)
      print(f"Jogada do Computador é {computer}")
      game = game.make_move(computer)
      game.draw_board()
    else:
      break
  
else:
  print("** VOCÊ JOGARÁ COM AS PEÇAS PRETAS **")
  while True:
    if not game.verify_game_over():
      computer = the_best_move(game,TREE_MAX_DEPT)
      print(f"Jogada do Computador é {computer}")
      game = game.make_move(computer)
      game.draw_board()
    else:
      break

    if not game.verify_game_over():
     game.verify_check()
     game = game.human_move()
     game.draw_board()
    else:
        break
