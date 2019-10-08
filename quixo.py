import copy


class Quixo:

    def __init__(self):
        self.board = [[0 for x in range(5)] for y in range(5)]
        self.edges = [(100, 100),
                      (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                      (1, 4), (2, 4), (3, 4), (4, 4),
                      (4, 3), (4, 2), (4, 1), (4, 0),
                      (3, 0), (2, 0), (1, 0)]

    def modify_board(self, origin, destiny, player):
        if origin == destiny:
            self.board[origin[0]][origin[1]] = player
        elif origin[1] < destiny[1]:
            self.push_line_left(player, origin[0], abs(origin[0] - destiny[0])) #izquierda
        elif origin[1] > destiny[1]:
            self.push_line_right(player, origin[0], abs(origin[0] - destiny[0])) #derecha
        elif origin[0] < destiny[0]:
            self.push_column(1) #abajo
        else:
            self.push_column(0) #arriba

    def push_column(self, direction):
        pass

    def push_line_right(self, player, line, delta):
        new_line = copy.deepcopy(self.board[line])
        new_line[0] = player
        for x in range(1, delta + 1):
            new_line[x] = self.board[line][x - 1]
        self.board[line] = new_line

    def push_line_left(self, player, line, delta):
        new_line = copy.deepcopy(self.board[line])
        new_line[4] = player
        for x in range(delta + 1, 4):
            new_line[x] = self.board[line][x + 1]
        self.board[line] = new_line

    def player_play(self):
        pass

    def valid_movement(self, origin, destiny, player):
        return (origin[0] == destiny[0] or origin[1] == destiny[1]) and\
               (self.board[origin[0]][origin[1]] == player or self.board[origin[0]][origin[1]] == 0)

    def opponent_play(self, move):
        origin = self.edges[move[0]]
        destiny = self.edges[move[1]]
        player = -1

        if not self.valid_movement(origin, destiny, player):
            raise Exception("Invalid movement of the opponent")

        self.modify_board(origin, destiny, player)

    def print_board(self):
        for y in range (5):
            print(end="| ")
            for x in range(5):
                print(self.board[y][x], end=" | ")
            print("\n")

if __name__ == '__main__':
    game = Quixo()

    move = (15, 7)
    game.opponent_play(move)
    move2 = (7, 15)
    game.opponent_play(move2)


    game.print_board()

