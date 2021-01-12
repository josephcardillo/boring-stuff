def move(x_or_o):
    player_move = input(f"{players[x_or_o]} choose your move > ").upper()
    return move

def validate_move(player_move):
    try:
        player_move in range(9)
        return True
    except KeyError:
        return False

players = ('X', 'JOE', 'O', 'SAM')
