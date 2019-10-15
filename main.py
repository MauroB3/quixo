from quixo import Quixo
from heuristic import check_horizontal

game = Quixo()

move = (1, 1)
game.apply_move(move, 1)
move = (2, 1)
game.apply_move(move, 1)
move = (2, 5)
game.apply_move(move, 1)
move = (4, 5)
game.apply_move(move, 1)
move = (3, 5)
game.apply_move(move, 1)
move = (2, 5)
game.apply_move(move, 1)


game.print_board()

print(check_horizontal(game.board[0], 1))


