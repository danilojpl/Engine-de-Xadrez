from Game import Game

game = Game()
moves = game.get_next_moves()

game.draw_board()
game.make_move(moves[0])
game.draw_board()

print('\n')
for r in game.board_array:
    for c in r:
      print(c, end = " ")
    print()
