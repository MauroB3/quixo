def heuristic(game, player):
   return check_horizontal(game, player) + check_vertical(game, player)


def check_horizontal(game, player):
    score = 0
    best_score = 0
    for y in range(5):
        for x in range(5):
            if game.board[y][x] == player:
                score += 1
                if score > best_score:
                    best_score = score
            else:
                score = 0
    return best_score


def check_vertical(game, player):
    score = 0
    best_score = 0
    for x in range(5):
        for y in range(5):
            if game.board[y][x] == player:
                score += 1
                if score > best_score:
                    best_score = score
            else:
                score = 0
    return best_score

