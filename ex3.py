def checkline(game, x):
    if game[x][0] == game[x][1] == game[x][2] == 1:
        return 1
    elif game[x][0] == game[x][1] == game[x][2] == 2:
        return 2
    else:
        return 0


def checkcol(game, y):
    if game[0][y] == game[1][y] == game[2][y] == 1:
        return 1
    elif game[0][y] == game[1][y] == game[2][y] == 2:
        return 2
    else:
        return 0


def checkcross(game):
    if game[1][1] == game[2][2] == game[0][0] == 1 or game[0][2] == game[1][1] == game[2][0] == 1:
        return 1
    elif game[1][1] == game[2][2] == game[0][0] == 2 or game[0][2] == game[1][1] == game[2][0] == 2:
        return 2
    else:
        return 0


if __name__ == '__main__':
    game = [[1, 2, 0],
            [2, 1, 0],
            [2, 1, 1]]
    checkline(game, 0)
    checkline(game, 1)
    checkline(game, 2)
    checkcol(game, 0)
    checkcol(game, 1)
    checkcol(game, 2)
    checkcross(game)

