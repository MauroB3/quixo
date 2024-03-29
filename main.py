from src.bailon_eiroa_quixo import Bailon_eiroa_quixo


def play():
    game = Bailon_eiroa_quixo()
    player = 1
    while not game.game_over():
        game.print_board()
        if player == -1:
            print("Turno del jugador -1")
            origin = int(input("Origen: "))
            destiny = int(input("Destino: "))
            move = (origin, destiny)
            game.opponentPlay(move)
            player = 1
        else:
            move = game.playerPlay()
            player = -1
            print("Movimiento IA: ", move)


play()

