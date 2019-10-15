import copy
from math import inf


class IAPlayer:

    def get_next_move(self):
        pass

    def alphabeta(self, game, player, depth, h, alpha=0, beta=0):
        best_move = (-1, -1)
        if player == 1:
            for move in game.possible_movements(player):
                child = copy.deepcopy(game)
                child.apply_move(move, player)
                score = self.max_score(game, player, depth, h)
                print(score)
                if score > alpha:
                    alpha = score
                    best_move = move
            return best_move
        else:
            best_move = (-1, -1)
            for move in game.possible_movements(player):
                child = copy.deepcopy(game)
                child.apply_move(move, player)
                score = self.min_score(game, player, depth, h)
                if score < beta:
                    beta = score
                    best_move = move
            return best_move

    def max_score(self, game, player, depth, h):
        if depth == 0:
            return h(game)

        score = 0
        for move in game.possible_movements(player):
            child = copy.deepcopy(game)
            child.apply_move(move, player)
            current_score = self.max_score(child, player, depth - 1, h)
            if current_score > score:
                score = current_score
        return score

    def min_score(self, game, player, depth, h):
        if depth == 0:
            return -h(game)

        score = 0
        for move in game.possible_movements(player):
            child = copy.deepcopy(game)
            child.apply_move(move, player)
            current_score = self.max_score(child, player, depth - 1, h)
            if current_score < score:
                score = current_score
        return score




