import chess
from Game import Game


i = 0
def minimax_alfabeta(game,turnMax,player_color, depth = 3, alfa = -9999, beta = 9999):
    if depth == 0:
        return game.calc_utility(player_color)

    if turnMax: #turno da IA
        alfa = -9999
        for nextMove in game.get_next_moves():
            utility = minimax_alfabeta (game.make_move(nextMove), False,player_color, depth-1, alfa, beta)
            alfa = max(utility, alfa)
            if beta <= alfa:
                return alfa
        return alfa
    else: #turno do min
        for nextMove in game.get_next_moves():
            utility = minimax_alfabeta(game.make_move(nextMove), True,player_color, depth-1, alfa, beta)
            beta = min(utility, beta)
            if beta <= alfa:
                return beta
        return beta
    


def the_best_move (game,depth = 3):
    best_value = float("-inf")
    best_move = -1	
    for nextMove in game.get_next_moves(): 
        utility = minimax_alfabeta(game.make_move(nextMove),False, game.board.turn, depth) 
        if utility > best_value:
            best_value = utility
            best_move = nextMove
    return best_move
    







