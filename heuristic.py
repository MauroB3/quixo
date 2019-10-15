def heuristic(game, player):
    score = check_horizontal(game) + check_vertical(game)


def check_horizontal(line, player):
    score = 0
    best_score = 0
    for x in range(5):
        if line[x] == player:
            score += 1
            if score > best_score:
                best_score = score
        else:
            score = 0
    return best_score

def check_vertical(ad):
    score = 0
    best_score = 0
    for x in range(5):
        if line[x] == player:
            score += 1
            if score > best_score:
                best_score = score
        else:
            score = 0
    return best_score

