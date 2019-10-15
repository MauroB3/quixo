import copy
from math import inf


class IAPlayer:

    def get_next_move(self):
        pass

    def alphabeta(self, game, depth, player, h, alpha=inf, beta=-inf):
        best_move = (-1, -1)
        if player == 1: # max
            for move in game.possible_movements(player):
                child = copy.deepcopy(game)
                child.apply_move(move)
                score = 0
                if score > alpha:
                    alpha = score
                    best_move = move
            return best_move
        else:
            # min
            best_move = (-1, -1)
            for move in game.possible_movements(player):
                child = copy.deepcopy(game)
                child.apply_move(move)
                score = 0
                if score < beta:
                    beta = score
                    best_move = move
            return best_move

