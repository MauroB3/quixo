def heuristic(game, player):

    score = cells_of_player(game, player) * 2 \
           + value_of_all_rows(game, player) \
           + value_of_all_columns(game, player) \
           + value_of_diagonals(game, player) \
           + value_if_is_win(game, player)
    return score


def value_if_is_win(game, player):
    if game.game_over():
        if game.winner == player:
            return 1000
        else:
            return -1000
    else:
        return 0


def cells_of_player(game, player):
    result = 0
    for y in range(5):
        for x in range(5):
            if game.board[y][x] == player:
                result += 1
    return result


def value_of_all_rows(game, player):
    score = 0
    for raw in range(5):
        score += value_of_list(game.board[raw], player)
    return score


def value_of_all_columns(game, player):
    score = 0
    for column in range(5):
        score += value_of_list(game.get_column(column), player)
    return score


def value_of_diagonals(game, player):
    diagonal_a = [game.board[0][0], game.board[1][1], game.board[2][2], game.board[3][3], game.board[4][4]]
    diagonal_b = [game.board[4][0], game.board[3][1], game.board[2][2], game.board[1][3], game.board[0][4]]
    return value_of_list(diagonal_a, player) + value_of_list(diagonal_b, player)


def value_of_list(listc, player):
    score = 0
    best_score = 0
    for pos in range(5):
        if listc[pos] == player:
            score += 1
            best_score = max(best_score, score)
        else:
            score = 0
    return best_score * 2
