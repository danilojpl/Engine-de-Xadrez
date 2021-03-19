from __config import TREE_MAX_DEPT, SQUARES_WEIGHTS, HEURISTICS, PIECES_WEIGHTS
from Game import Game
from minimax import the_best_move


#iniciando o jogo
game = Game()
while True:
  game = game.human_move()
  computer = the_best_move(game,TREE_MAX_DEPT)
  print(f"Jogada do Computador é {computer}")
  game = game.make_move(computer)
  game.draw_board()
  

