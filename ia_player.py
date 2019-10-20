import copy
from math import inf


class IAPlayer:

    def get_next_move(self):
        pass

    def alphabeta(self, game, player, depth, h, alpha=-inf, beta=inf):
        best_move = (-1, -1)
        if player == 1:
            for move in game.possible_movements(player):
                child = copy.deepcopy(game)
                child.apply_move(move, player)
                score = self.max_score(game, player, depth, h, alpha, beta)
                if score > alpha:
                    alpha = score
                    best_move = move
            return best_move
        else:
            for move in game.possible_movements(player):
                child = copy.deepcopy(game)
                child.apply_move(move, player)
                score = self.min_score(game, player, depth, h, alpha, beta)
                if score < beta:
                    beta = score
                    best_move = move
            return best_move

    def max_score(self, game, player, depth, h, alpha, beta):
        if depth == 0:
            return h(game, player)

        for move in game.possible_movements(player):
            child = copy.deepcopy(game)
            child.apply_move(move, player)
            current_score = self.min_score(child, -player, depth - 1, h, alpha, beta)
            if current_score > alpha:
                alpha = current_score
                if current_score >= beta:
                    break
        return alpha

    def min_score(self, game, player, depth, h, alpha, beta):
        if depth == 0:
            return h(game, player)

        for move in game.possible_movements(player):
            child = copy.deepcopy(game)
            child.apply_move(move, player)
            current_score = self.max_score(child, -player, depth - 1, h, alpha, beta)
            if current_score < beta:
                beta = current_score
                if current_score <= alpha:
                    break
        return beta




