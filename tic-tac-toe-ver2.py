game_board = {'TL': ' ', 'TM': ' ', 'TR': ' ',
              'ML': ' ', 'MM': ' ', 'MR': ' ',
              'BL': ' ', 'BM': ' ', 'BR': ' '}

def print_board(board):
    print()
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    if board['TL'] == 'TL':
        print('--+--+--')
    else:
        print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    if board['TL'] == 'TL':
        print('--+--+--')
    else:
        print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])
    print()

turn = 'X'

for i in range(9):
    print_board(game_board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    game_board[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn == 'X'

print_board(game_board)