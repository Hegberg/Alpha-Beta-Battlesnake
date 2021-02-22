import random

from algorithms.alpha_beta import AlphaBeta
from algorithms.common import print_board


DEBUG = False

def get_move(data):

    alpha_beta = AlphaBeta(data)
    alpha = alpha_beta.alpha_start
    beta = alpha_beta.beta_start
    value = alpha_beta.alpha_beta_breadth_first_search_loop(alpha_beta.data['board'], alpha_beta.max_depth, alpha, beta)

    best_move = None
    if ('snakes' in alpha_beta.best_boards[0]):
        best_move = alpha_beta.get_move_from_new_board(alpha_beta.best_boards[0])
    else:
        temp_board = move = random.choice(alpha_beta.base_boards)
        best_move = alpha_beta.get_move_from_new_board(temp_board)


    if (not best_move == None):
        if DEBUG:
            print_board(data, data['board'])
            print('Best move: ' + str(best_move) + "    --Value: " + str(value))
            print("Nodes hit: " + str(alpha_beta.nodes_evaluated))
            print("Nodes predicted: " + str(alpha_beta.predictive_nodes))
        return best_move
    else:
        if DEBUG:
            print('No best move: ' + str(best_move))
        possible_moves = ["up", "down", "left", "right"]
        move = random.choice(possible_moves)
        return move