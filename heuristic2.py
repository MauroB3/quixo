def heuristic(game, player):
    return cells_of_player(game, player) \
           + value_of_all_rows(game, player) \
           + value_of_all_columns(game, player)


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


def value_of_list(list, player):
    score = 0
    best_score = 0
    for pos in range(5):
        if list[pos] == player:
            score += 1
            best_score = max(best_score, score)
        else:
            score = 0
    return best_score
