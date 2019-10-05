class Quixo:

    def __init__(self):
        self.board = [[0 for x in range(5)] for y in range(5)]
        self.dict = self.create_dict()

    def create_dict(self):
        temp_dict = []
        temp_dict[1] = (0,0)
        temp_dict[2] = (0, 1)
        temp_dict[3] = (0, 2)
        temp_dict[4] = (0, 3)
        temp_dict[5] = (0, 4)
        temp_dict[6] = (1, 4)
        temp_dict[7] = (2, 4)
        temp_dict[8] = (3, 4)
        temp_dict[9] = (4, 4)
        temp_dict[10] = (4, 3)
        temp_dict[11] = (4, 2)
        temp_dict[12] = (4, 1)
        temp_dict[13] = (4, 0)
        temp_dict[14] = (3, 0)
        temp_dict[15] = (2, 0)
        temp_dict[16] = (1, 0)
        return temp_dict

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


    def push_line(self, direction):


    def player_play(self):
        pass

    def oponent_play(self, move):
        origin = self.dict[move[0]]
        destiny = self.dict[move[1]]
        self.modify_board(origin, destiny)
        pass

