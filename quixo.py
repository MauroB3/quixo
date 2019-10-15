import itertools

class Quixo:

    def __init__(self):
        self.board = [[0 for x in range(5)] for y in range(5)]
        self.edges = [
                      (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                      (1, 4), (2, 4), (3, 4), (4, 4),
                      (4, 3), (4, 2), (4, 1), (4, 0),
                      (3, 0), (2, 0), (1, 0)]

    def modify_board(self, origin, destiny, player):
        if origin == destiny:
            self.board[origin[0]][origin[1]] = player
        elif origin[0] < destiny[0]:
            self.push_column_up(player, origin[1], origin[0], destiny[0]) #abajo
        elif origin[0] > destiny[0]:
            self.push_column_down(player, origin[1], origin[0], destiny[0]) #arriba
        else:
            self.push_line(player, origin[0], origin[1], destiny[1])

    def push_column_up(self, player, column, origin, destiny):
        self.board[origin][column] = player
        for line in range(origin, destiny):
            self.board[line][column], self.board[line + 1][column] = self.board[line + 1][column], self.board[line][column]

    def push_column_down(self, player, column, origin, destiny):
        self.board[origin][column] = player
        for line in reversed(range(destiny + 1, origin + 1)):
            self.board[line][column], self.board[line - 1][column] = self.board[line - 1][column], self.board[line][column]

    def push_line(self, player, line, origin, next_position):
        self.board[line].pop(origin)
        self.board[line].insert(next_position, player)

    def possible_destinations(self, origin):
        y, x = self.edges[origin - 1]
        destinations = [(origin, origin),
                        (origin, self.edges.index((y, 0)) + 1), (origin, self.edges.index((y, 4)) + 1),
                        (origin, self.edges.index((0, x)) + 1), (origin, self.edges.index((4, x)) + 1)]
        return list(dict.fromkeys(destinations))

    def possible_movements(self, player):
        result = []
        index = 0
        for cell in self.edges:
            index += 1
            if self.cell_available_for_player(cell, player):
                result += self.possible_destinations(index)
        return result

    def possible_movements2(self, player):
        return list(itertools.chain.from_iterable(map(lambda cell: self.possible_destinations(self.edges.index(cell) + 1) if self.cell_available_for_player(cell, player) else [], self.edges)))

    def valid_movement(self, origin, destiny, player):
        return destiny in self.edges and \
                origin in self.edges and \
                (self.edges.index(origin), self.edges.index(origin)) in self.possible_destinations(self.edges.index(origin)) and \
                self.cell_available_for_player(origin, player)

    def cell_available_for_player(self, cell, player):
        return self.board[cell[0]][cell[1]] == player or self.board[cell[0]][cell[1]] == 0

    def opponent_play(self, movement):
        origin = self.edges[movement[0] - 1]
        destiny = self.edges[movement[1] - 1]
        player = -1

        if not self.valid_movement(origin, destiny, player):
            raise Exception("Invalid movement of the opponent")

        self.modify_board(origin, destiny, player)

    def player_play(self):
        pass

    def print_board(self):
        for row in range(len(self.board)):
            print('+' + '-----+'*len(self.board[0]))
            print('|', end='  ')
            for col in range(len(self.board[row])):
                print(self.board[row][col], end='  |  ')
            print('')
        print('+-----'*(len( self.board[0])) + '+')
