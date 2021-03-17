import chess
from Game import Game
from __config import TREE_MAX_DEPT


def minimax_alfabeta(move,turnMax, depth = 6, alfa = float("-inf"), beta = float("inf")):
    if depth == 0:
        if chess.WHITE:
            return move.calc_utility("WHITE")
        else:
            return move.calc_utility("BLACK")

    if turnMax: #turno da IA
        for nextMove in move.get_next_moves():
            print(nextMove)
            utility = minimax_alfabeta (move.make_move(nextMove), False, depth-1, alfa, beta)
            alfa = max(utility, alfa)
            if beta <= alfa:
                break
            return alfa
    else: #turno do min
        for nextMove in move.get_next_moves():
            utility = minimax_alfabeta(move.make_move(nextMove), True, depth-1, alfa, beta)
            beta = min(utility, beta)
            if beta <= alfa:
                break
            return beta


def the_best_move (game,depth = 6):
    best_value = float("-inf")
    best_move = -1
    for nextMove in game.get_next_moves():
        utility = minimax_alfabeta(game.make_move(nextMove), False, depth)
        if utility > best_value:
            best_value = utility
            best_move = nextMove
    return best_move
    







