from copy import deepcopy
from math import inf


class IAPlayer:

    def __init__(self):
        self.current_movement_number = 0

    def get_next_move(self):
        pass

    def alphabeta(self, game, h, player, alpha=-inf, beta=inf):
        depth = self.next_depth()
        if player == -1:
            legal_moves = game.possible_movements(-1)
            if not legal_moves:
                return -1, -1
            best_current_move = legal_moves[0]
            for move in legal_moves:
                child = deepcopy(game)
                child.apply_move(move, -1)
                score = self.max_score(child, h, depth - 1, alpha, beta)
                if score > alpha:
                    alpha = score
                    best_current_move = move
            return best_current_move
        else:
            legal_moves = game.possible_movements(1)
            if not legal_moves:
                return -1, -1
            best_current_move = legal_moves[0]
            for move in legal_moves:
                child = deepcopy(game)
                child.apply_move(move, 1)
                score = self.min_score(child, h, depth - 1, alpha, beta)
                if score < beta:
                    beta = score
                    best_current_move = move
            return best_current_move

    def max_score(self, game, h, depth, alpha, beta):
        if depth == 0:
            return h(game, -1)
        legal_moves = game.possible_movements(1)
        for move in legal_moves:
            child = deepcopy(game)
            child.apply_move(move, 1)
            score = self.min_score(child, h, depth - 1, alpha, beta)
            if score > alpha:
                alpha = score
                if alpha >= beta:
                    break
        return alpha

    def min_score(self, game, h, depth, alpha, beta):
        if depth == 0:
            return h(game, -1)
        legal_moves = game.possible_movements(-1)
        for move in legal_moves:
            child = deepcopy(game)
            child.apply_move(move, -1)
            score = self.max_score(child, h, depth - 1, alpha, beta)
            if score < beta:
                beta = score
                if beta <= alpha:
                    break
        return beta

    def next_depth(self):
        self.current_movement_number += 1
        if self.current_movement_number < 4:
            return 1
        else:
            if self.current_movement_number < 6:
                return 2
            else:
                return 3




