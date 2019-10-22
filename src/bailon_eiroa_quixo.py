from copy import deepcopy
from math import inf


class Bailon_eiroa_quixo:
    def __init__(self):
        self.board = [[0 for x in range(5)] for y in range(5)]
        self.edges = [
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
            (1, 4), (2, 4), (3, 4), (4, 4),
            (4, 3), (4, 2), (4, 1), (4, 0),
            (3, 0), (2, 0), (1, 0)]
        self.winner = 0
        self.ia_player = IAPlayer()

    def __eq__(self, other):
        return self.board == other.board

    def modify_board(self, origin, destiny, player):
        if origin == destiny:
            self.board[origin[0]][origin[1]] = player
        elif origin[0] < destiny[0]:
            self.push_column_up(player, origin[1], origin[0], destiny[0])  # abajo
        elif origin[0] > destiny[0]:
            self.push_column_down(player, origin[1], origin[0], destiny[0])  # arriba
        else:
            self.push_line(player, origin[0], origin[1], destiny[1])

    def apply_move(self, move, player):
        origin = self.edges[move[0] - 1]
        destiny = self.edges[move[1] - 1]
        self.modify_board(origin, destiny, player)

    def push_column_up(self, player, column, origin, destiny):
        self.board[origin][column] = player
        for line in range(origin, destiny):
            self.board[line][column], self.board[line + 1][column] = self.board[line + 1][column], self.board[line][
                column]

    def push_column_down(self, player, column, origin, destiny):
        self.board[origin][column] = player
        for line in reversed(range(destiny + 1, origin + 1)):
            self.board[line][column], self.board[line - 1][column] = self.board[line - 1][column], self.board[line][
                column]

    def push_line(self, player, line, origin, next_position):
        self.board[line].pop(origin)
        self.board[line].insert(next_position, player)

    def possible_destinations(self, origin):
        y, x = self.edges[origin - 1]
        destinations = [
            (origin, self.edges.index((y, 0)) + 1), (origin, self.edges.index((y, 4)) + 1),
            (origin, self.edges.index((0, x)) + 1), (origin, self.edges.index((4, x)) + 1)]
        #if self.board[y][x] != 0:
        #    destinations.remove((origin, origin))

        return list(dict.fromkeys(destinations))

    def possible_movements(self, player):
        result = []
        index = 0
        for cell in self.edges:
            index += 1
            if self.cell_available_for_player(cell, player):
                result += self.possible_destinations(index)
        return list(filter(lambda m: self.valid_movement(self.edges[m[0] - 1], self.edges[m[1] - 1], player), result))

    def valid_movement(self, origin, destiny, player):
        origin_index = self.edges.index(origin) + 1
        destiny_index = self.edges.index(destiny) + 1
        return destiny in self.edges and \
               origin in self.edges and \
               (origin_index, destiny_index) in self.possible_destinations(origin_index) and \
               self.cell_available_for_player(origin, player) and \
               self.move_modify_board(origin, destiny, player)

    def move_modify_board(self, origin, destiny, player):
        origin = self.edges.index(origin) + 1
        destiny = self.edges.index(destiny) + 1
        new_board = deepcopy(self)
        new_board.apply_move((origin, destiny), player)
        return self != new_board

    def cell_available_for_player(self, cell, player):
        return self.board[cell[0]][cell[1]] == player or self.board[cell[0]][cell[1]] == 0

    def opponentPlay(self, movement):
        origin = self.edges[movement[0] - 1]
        destiny = self.edges[movement[1] - 1]
        player = -1

        if not self.valid_movement(origin, destiny, player):
            raise Exception("Invalid movement of the opponent")

        self.modify_board(origin, destiny, player)

    def playerPlay(self):
        move = self.ia_player.get_next_move(self, heuristic, 1)
        self.apply_move(move, 1)
        return move

    def game_over(self):
        return self.check_vertical_win() or \
               self.check_horizontal_win() or \
               self.check_diagonal_one_win() or \
               self.check_diagonal_two_win()

    def is_winner(self, player):
        return self.game_over() and self.winner == player

    def game_over_for_player(self, player):
        return self.game_over() and self.winner == -player

    def check_vertical_win(self):
        for y in range(5):
            if ((self.board[0][y] != 0) and
                    (self.board[0][y] ==
                     self.board[0 + 1][y] ==
                     self.board[0 + 2][y] ==
                     self.board[0 + 3][y] ==
                     self.board[0 + 4][y])):
                self.winner = self.board[0][y]
                return True
        return False

    def check_horizontal_win(self):
        for x in range(5):
            if ((self.board[x][0] != 0) and
                    (self.board[x][0] ==
                     self.board[x][0 + 1] ==
                     self.board[x][0 + 2] ==
                     self.board[x][0 + 3] ==
                     self.board[x][0 + 4])):
                self.winner = self.board[x][0]
                return True
        return False

    def check_diagonal_one_win(self):
        if (self.board[0][0] != 0 and
                (self.board[0][0]
                 == self.board[1][1]
                 == self.board[2][2]
                 == self.board[3][3]
                 == self.board[4][4])):
            self.winner = self.board[0][0]
            return True
        else:
            return False

    def check_diagonal_two_win(self):
        if (self.board[0][4] != 0 and
                (self.board[0][4]
                 == self.board[1][3]
                 == self.board[2][2]
                 == self.board[3][1]
                 == self.board[4][0])):
            self.winner = self.board[0][4]
            return True
        else:
            return False

    def borders_available(self):
        result = 0
        for e in self.edges:
            if self.board[e[0]][e[1]] == 0:
                result += 1
        return result

    def get_column(self, number):
        column = []
        for y in range(5):
            column.append(self.board[y][number])
        return column

    def play(self, time):
        return self.playerPlay()

    def update(self, move):
        self.opponentPlay(move)

    @staticmethod
    def translate_position(pos):
        if pos > 0:
            return 'X'
        else:
            if pos < 0:
                return 'O'
            else:
                return '-'

    def print_board(self):
        for row in range(len(self.board)):
            print('+' + '-----+' * len(self.board[0]))
            print('|', end='  ')
            for col in range(len(self.board[row])):
                print(self.translate_position(self.board[row][col]), end='  |  ')
            print('')
        print('+-----' * (len( self.board[0])) + '+')





class IAPlayer:

    def __init__(self):
        self.current_movement_number = 0

    def get_next_move(self, game, h, player):
        return self.alphabeta(game, h, player)

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
        if depth == 0 or game.game_over():
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
        if depth == 0 or game.game_over():
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
            return 3




def value_if_is_win(game, player):
    if game.game_over():
        if game.winner == player:
            return 1000
        else:
            return -1000
    else:
        return 0


def cells_of_player(game, player):
    result = 0
    for y in range(5):
        for x in range(5):
            if game.board[y][x] == player:
                result += 1
    return result


def value_of_all_rows(game, player):
    score = 0
    for raw in range(5):
        score += value_of_list(game.board[raw], player)
    return score


def value_of_all_columns(game, player):
    score = 0
    for column in range(5):
        score += value_of_list(game.get_column(column), player)
    return score


def value_of_diagonals(game, player):
    diagonal_a = [game.board[0][0], game.board[1][1], game.board[2][2], game.board[3][3], game.board[4][4]]
    diagonal_b = [game.board[4][0], game.board[3][1], game.board[2][2], game.board[1][3], game.board[0][4]]
    return max(value_of_list(diagonal_a, player), value_of_list(diagonal_b, player))


def value_of_list(listc, player):
    score = 0
    best_score = 0
    for pos in range(5):
        if listc[pos] == player:
            score += 1
            best_score = max(best_score, score)
        else:
            score = 0
    return best_score * best_score


def heuristic(game, player):
    cells = cells_of_player(game, player)
    if cells >= 2:
        return cells * 10 \
               + value_of_all_rows(game, player) \
               + value_of_all_columns(game, player) \
               + value_of_diagonals(game, player) * 0.5 \
               + value_if_is_win(game, player)
    else:
        return 1
