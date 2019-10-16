from quixo import Quixo


def play():
    game = Quixo()
    player = -1
    while not game.game_over():
        print('\n' * 80)
        game.print_board()
        if player == -1:
            print("Turno del jugador -1")
            origin = int(input("Origen: "))
            destiny = int(input("Destino: "))
            move = (origin, destiny)
            game.apply_move(move, player)
            player = 1
        else:
            move = game.player_play()
            game.apply_move(move, player)
            player = -1


play()


