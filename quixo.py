class Quixo:

    def __init__(self):
        self.board = [[0 for x in range(5)] for y in range(5)]
        self.edges = [(100, 100),
                      (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                      (1, 4), (2, 4), (3, 4), (4, 4),
                      (4, 3), (4, 2), (4, 1), (4, 0),
                      (3, 0), (2, 0), (1, 0)]

    def modify_board(self, origin, destiny):
        if self.board[origin[0]][origin[1]] == 0:
            self.board[origin[0]][origin[1]] = -1
        elif origin[0] > destiny[0]:
            self.push_line(0) #izquierda
        elif origin[0] < destiny[0]:
            self.push_line(1) #derecha
        elif origin[1] > destiny[1]:
            self.push_column(1) #arriba
        else:
            self.push_column(0) #abajo

    def push_column(self, direction):
        pass

    def push_line(self, direction):
        pass

    def player_play(self):
        pass

    def check_movement(self, move):
        pass

    @staticmethod
    def valid_movement(self, origin, destiny):
        return origin[0] == destiny[0] or origin[1] == destiny[1]

    def opponent_play(self, move):
        origin = self.edges[move[0]]
        destiny = self.edges[move[1]]

        if not self.valid_movement(origin, destiny):
            raise Exception("Invalid movement of the opponent")

        self.modify_board(origin, destiny)


    def printBoard(self):
        for row in range(len(self.board)):
            print('+' + '-----+'*len(self.board[0]))
            print('|', end='  ')
            for col in range(len(self.board[row])):
                print(self.board[row][col], end='  |  ')
            print('')
        print('+-----'*(len( self.board[0])) + '+')


if __name__ == '__main__':
    q = Quixo()
    q.printBoard()
