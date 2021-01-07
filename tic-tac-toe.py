

game_board = {'TL': ' ', 'TM': ' ', 'TR': ' ',
                'ML': ' ', 'MM': ' ', 'MR': ' ',
                'BL': ' ', 'BM': ' ', 'BR': ' '}

game_board_positions = {'TL': 'TL', 'TM': 'TM', 'TR': 'TR',
                        'ML': 'ML', 'MM': 'MM', 'MR': 'MR',
                        'BL': 'BL', 'BM': 'BM', 'BR': 'BR'}

play = input("Hello. Would you like to play Tic-Tac-Toe? Y or N > ")

def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def init_players():
    player1_pick = ' '
    while player1_pick != 'X' and player1_pick != 'O':
        player1_pick = input("Player 1, choose X or O > ")
    print(f"Player 1 is > {player1_pick}")
    player1_name = input("Player 1 name > ")
    if player1_pick == 'X':
        player2_pick = 'O'
    else:
        player2_pick = 'X'
    print(f"Player 2 is > {player2_pick}")
    player2_name = input("Player 2 name > ")
    return player1_pick, player1_name, player2_pick, player2_name

if play == 'Y':
    players = init_players()
else:
    print('Goodbye.')
    exit()

print("Players can choose the following positions during game play:")
print_board(game_board_positions)


def check_win():
    if game_board['TL'] == 'X' and game_board['TM'] == 'X' and game_board['TR'] == 'X':
        return True
    elif game_board['ML'] == 'X' and game_board['MM'] == 'X' and game_board['MR'] == 'X':
        return True
    elif game_board['BL'] == 'X' and game_board['BM'] == 'X' and game_board['BR'] == 'X':
        return True
    elif game_board['TL'] == 'O' and game_board['TM'] == 'O' and game_board['TR'] == 'O':
        return True
    elif game_board['ML'] == 'O' and game_board['MM'] == 'O' and game_board['MR'] == 'O':
        return True
    elif game_board['BL'] == 'O' and game_board['BM'] == 'O' and game_board['BR'] == 'O':
        return True
    elif game_board['TL'] == 'X' and game_board['ML'] == 'X' and game_board['BL'] == 'X':
        return True
    elif game_board['TM'] == 'X' and game_board['MM'] == 'X' and game_board['BM'] == 'X':
        return True
    elif game_board['TR'] == 'X' and game_board['MR'] == 'X' and game_board['BR'] == 'X':
        return True
    elif game_board['TL'] == 'O' and game_board['ML'] == 'O' and game_board['BL'] == 'O':
        return True
    elif game_board['TM'] == 'O' and game_board['MM'] == 'O' and game_board['BM'] == 'O':
        return True
    elif game_board['TR'] == 'O' and game_board['MR'] == 'O' and game_board['BR'] == 'O':
        return True
    elif game_board['TL'] == 'X' and game_board['MM'] == 'X' and game_board['BR'] == 'X':
        return True
    elif game_board['TR'] == 'X' and game_board['MM'] == 'X' and game_board['BL'] == 'X':
        return True
    elif game_board['TL'] == 'O' and game_board['MM'] == 'O' and game_board['BR'] == 'O':
        return True
    elif game_board['TR'] == 'O' and game_board['MM'] == 'O' and game_board['BL'] == 'O':
        return True
    else:
        return False


for i in range(9):
    if i % 2 == 0:
        player1_move = input(f"{players[1]} choose your move > ")
        while game_board[player1_move] != ' ':
            print(f"Can't play at {player1_move}")
            player1_move = input(f"{players[1]} choose your move > ")
        print(f"Move is > {player1_move}")
        game_board[player1_move] = players[0]
        print_board(game_board)
        if check_win() == True:
            print(f"{players[1]} wins!")
            break
    else:
        player2_move = input(f"{players[3]} choose your move > ")
        while game_board[player2_move] != ' ':
            print(f"Can't play at {player2_move}")
            player2_move = input(f"{players[3]} choose your move > ")
        print(f"Move is > {player2_move}")
        game_board[player2_move] = players[2]
        print_board(game_board)
        if check_win() == True:
            print(f"{players[3]} wins!")
            break

# game_play(players, game_board)

