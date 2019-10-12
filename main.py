from quixo import Quixo

game = Quixo()

move = (15, 1)
game.opponent_play(move)
move = (1, 13)
game.opponent_play(move)

game.print_board()
