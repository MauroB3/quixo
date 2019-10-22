from src.heuristic import heuristic
from src.ia_player import IAPlayer
from copy import deepcopy


class Quixo:

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
        return destiny in self.edges and \
            origin in self.edges and \
            (origin_index, origin_index) in self.possible_destinations(origin_index) and \
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
        move = self.ia_player.alphabeta(self, heuristic, 1)
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
        return self.playerPlay()  # noten que descarto el time, pero si lo quieren usar adelante

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


