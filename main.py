from quixo import Quixo


def play():
    game = Quixo()
    player = 1
    while not game.game_over():
        #print('\n' * 80)
        game.print_board()
        if player == -1:
            print("Turno del jugador -1")
            origin = int(input("Origen: "))
            destiny = int(input("Destino: "))
            move = (origin, destiny)
            game.opponent_play(move)
            player = 1
        else:
            move = game.player_play()
            player = -1
            print("Movimiento IA: ", move)


play()

'''
game = Quixo()
move = (1, 1)
game.apply_move(move, -1)
move = (5, 5)
game.apply_move(move, 1)
move = (16, 16)
game.apply_move(move, -1)
move = (4, 4)
game.apply_move(move, 1)
move = (15, 15)
game.apply_move(move, -1)
move = (3, 3)
game.apply_move(move, 1)
move = (14, 14)
game.apply_move(move, -1)
move = (2, 2)
game.apply_move(move, 1)

game.print_board()

print(game.player_play())
'''
