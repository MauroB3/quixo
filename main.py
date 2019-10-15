from quixo import Quixo

game = Quixo()


move = (1, 1)
game.opponent_play(move)
move = (2, 2)
game.opponent_play(move)
move = (3, 3)
game.opponent_play(move)
move = (4, 4)
game.opponent_play(move)
move = (5, 5)
game.opponent_play(move)


game.print_board()

print(game.check_vertical_win())