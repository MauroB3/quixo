from quixo import Quixo

game = Quixo()

move = (15, 7)
game.opponent_play(move)
move2 = (7, 15)
game.opponent_play(move2)


game.print_board()
